"""

A package to process minor problems in EXCEL documents of student
attendences in Nanjing Medical University                --by heyrict

MAKE SURE YOU HAVE INSTALLED 'PANDAS' BEFORE YOU USE THIS PACKAGE.
"""

import os
import pandas as pd
import numpy as np
from pandas import DataFrame, Series

def __stdiz__(stno,typ):
    """
    return a normalized data with a special type.
    """
    if typ == "int":
        if type(stno)!=int:
            x = stno.strip()
            if x[0]=="'":
               return int(x[1:])
            return int(x)
    if typ == "str":
        return str(stno.strip())
    if typ == "float":
        return float(stno)
    return stno


def __getnamefrompath__(path):
    """
    get the name of .xls(x) files.
    """
    path = str(path)
    return path[:-4] if path[-4:]==".xls" else path[:-5]


def __read__(filepath,inputfolder="",key=['学号','姓名'],
             keyformat=['int','str'],subkey=[]):
    """
    read a xls(x) file in filepath and return a pandas.DataFrame object
    with its column name normalized

    path of a xls(x) file -> pandas.core.frame.DataFrame

    arguments:
       filepath : string
           -- path of the excel file to read.
       key : list of string(s)
           -- the shared key of the file(s), which will appear in the merged
              excel file, default ['学号','姓名'].
       keyformat : list of string(s)
           -- the type of key, default ['int','str'].
               options:
                   'str', 'int', 'float'
       subkey : list of string(s)
           -- the shared subkey of the file(s), which will not appear in the
           merged excel file, default []
    """
    filename = __getnamefrompath__(filepath)
    fp = inputfolder + filepath
    df = pd.read_excel(fp)
    df.index = range(len(df))

    

    for k in key+subkey:
        if k not in df.columns:
            l = key+subkey+[filename]
            df = pd.read_excel(fp,names=l)
            df[filename] = df[filename].fillna(1)
            break
    if len(df.columns) <= len(key+subkey):
        df = DataFrame(df,columns=list(df.columns)+[filename])
    for i,j in zip(key,keyformat):
        df[i] = df[i].apply(lambda x:__stdiz__(x,j))

    t = df.columns.map(lambda x:True if(len(x)>7 and x[:8]=="Unnamed:")
                       else False)

    if t.any():
        loc = df.columns.get_loc(key[-1])+1
        for i in df.columns[loc:]:
            del df[i]
        df[filename] = 1

    
    for i in subkey:
        del df[i]
        
    return df


def join_list(lpath,key=['学号','姓名'],keyformat=['int','str'],subkey=[],
              inputfolder="input\\"):
    """
    merge a list of xls(x) into a new xls file.

    path list of xls(x) files -> pandas.core.frame.DataFrame
    
    arguments:
       lpath : list of string(s)
           -- list of excel file(s) to merge.
       key : list of string(s)
           -- the shared key of the file(s), which will appear in the merged
              excel file, default ['学号','姓名'].
       keyformat : list of string(s)
           -- the type of key, default ['int','str'].
               options:
                   'str', 'int', 'float'
       subkey : list of string(s)
           -- the shared subkey of the file(s), which will not appear in the
           merged excel file, default [].
       inputfolder : string
           -- the directory of lpath, default "input\\".
              please set it to "" if lpath has drive letter.
    """
    
    
    d = __read__(str(lpath[0]),inputfolder=str(inputfolder),key=key,subkey=subkey)
    for i in lpath[1:]:
        d = pd.merge(d,__read__(str(i),inputfolder=str(inputfolder),key=key,keyformat=keyformat,
                                subkey=subkey),on=key,how='outer')
    d.sort_index(axis=1)
    return d


def to_excel(df,filename="output.xls",key=["姓名","学号"]): 
    """
    output a DataFrame with a given name.

    arguments:
       df : pandas.core.frame.DataFrame
           -- the DataFrame object to output.
       filename : string
           -- name of the output file, default "output.xls"
       key : list of string(s)
           -- keys to sort by, default ["姓名","学号"].
    """
    out = str(filename)
    if out[-4:] not in ['.xls','xlsx']:
        out = out + '.xls'
    if not os.path.exists("output\\"):
        os.mkdir("output\\")
    df.sort_values(by=key).to_excel("output\\"+out,index=False)
    return


def merge_to_meta(df,metdata="meta_data\\meta.xlsx",how='left',
                   key=['学号','姓名'],keyformat=['int','str'],subkey=[]):
    """
    merge and compare a DataFrame to a database.

    pandas.core.frame.DataFrame -> pandas.core.frame.DataFrame
    
    arguments:
       df : pandas.core.frame.DataFrame
           -- the DataFrame object to get merged.
       metdata : string
           -- the path of meta data, default "meta_data\\meta.xlsx".
       how : string
           -- parameter used by pandas.merge implying the merge method,
               default 'left'.
       key : list of string(s)
           -- the shared key of the file(s), which will appear in the merged
              excel file, default ['学号','姓名'].
       keyformat : list of string(s)
           -- the type of key, default ['int','str'].
               options:
                   'str', 'int', 'float'
       subkey : list of string(s)
           -- the shared subkey of the file(s), which will not appear in the
           merged excel file, default [].
    """
    mt = pd.read_excel(metdata,names=key+subkey)
    for i,j in zip(key,keyformat):
        mt[i] = mt[i].apply(lambda x:__stdiz__(x,j))
    for i in subkey:
        del mt[i]
    return pd.merge(mt,df,how=how,on=key)


def find_duplicated(lpath,metdata="meta_data\\meta.xlsx",inputfolder="input\\",
                    key=['学号','姓名'],keyformat=['int','str'],subkey=[]):
    """
    return a DataFrame showing data in conflict with metadata.

    str -> pandas.core.frame.DataFrame

    arguments:
        lpath : string, list of string
            -- the path(s) of the xls(x) file.
        metdata : string
            -- the path of meta data, default "meta_data\\meta.xlsx".
        inputfolder : string
           -- the directory of lpath, default "input\\".
              please set it to "" if lpath has drive letter.
        key : list of string(s)
            -- the shared key of the file(s), which will appear in the merged
                    excel file, default ['学号','姓名'].
        keyformat : list of string(s)
            -- the type of key, default ['int','str'].
                options:
                    'str', 'int', 'float'
        subkey : list of string(s)
            -- the shared subkey of the file(s), which will not appear in the
            merged excel file, default [].
    """
    if type(lpath)==str:
        lpath = [lpath]
    mt = pd.read_excel(metdata,names=key+subkey)
    for i,j in zip(key,keyformat):
        mt[i] = mt[i].apply(lambda x:__stdiz__(x,j))
    mt['来源']='meta'
    
    l = list()
    em = DataFrame(columns=key)

    for xlspath in lpath:
        df = __read__(xlspath,inputfolder=inputfolder,key=key,keyformat=keyformat,
                        subkey=subkey)[key]
        t = pd.merge(mt,df,how='outer')
        em = pd.merge(em,t[t[key[0]].duplicated(keep=False)],how='outer').fillna(__getnamefrompath__(xlspath))
    return em.sort_values(by=key).set_index(key)
    
        

def total_process(lpath,key=['学号','姓名'],keyformat=['int','str'],subkey=[],
                  metdata="meta_data\\meta.xlsx",output="output.xls",
                  match=False,inputfolder="input\\"):
    """
    a packed function for get several excel files merged to one meta data.

    arguments:
       lpath : list of string(s)
           -- list of excel file(s) to merge.
       key : list of string(s)
           -- the shared key of the file(s), which will appear in the merged
              excel file, default ['学号','姓名'].
       keyformat : list of string(s)
           -- the type of key, default ['int','str'].
               options:
                   'str', 'int', 'float'
       subkey : list of string(s)
           -- the shared subkey of the file(s), which will not appear in the
           merged excel file, default [].
       metdata : string
           -- the path of meta data, default "meta_data\\meta.xlsx".
       output : string
           -- name of the output file, default "output.xls"
       match : bool
           -- whether to match the given files with the meta data, default False.
       inputfolder : string
           -- the directory of lpath, default "input\\".
              please set it to "" if lpath has drive letter.
    """
    lp = list(lpath)
    k = list(key)
    kf = list(keyformat)
    sk = list(subkey)
    mt = str(metdata)
    op = str(output)
    ip = str(inputfolder)
    
    df = join_list(lp,key=k,keyformat=kf,subkey=sk,inputfolder=ip)
    df = merge_to_meta(df,metdata=mt,how=('left' if match else 'outer'),
                        key=k,keyformat=kf,subkey=sk)
    to_excel(df,filename=op,key=k)
