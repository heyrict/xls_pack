"""

A package to process minor problems in EXCEL documents of student
attendences in Nanjing Medical University                --by Xie

MAKE SURE YOU HAVE INSTALLED 'PANDAS' BEFORE YOU USE THIS PACKAGE!!!
"""

import os
import pandas as pd
import numpy as np
from pandas import DataFrame, Series

def __stdiz__(stno,typ):
    if typ == "int":
        if type(stno)!=int:
            x = stno.strip()
            if x[0]=="'":
               return int(x[1:])
            return int(x)
    if typ == "str":
        return str(stno.strip())
    return stno


def __read__(filepath,key=['学号','姓名'],keyformat=['int','str'],subkey=[]):
    """
    read a xls(x) file in filepath and return a pandas.DataFrame object
    with its column name processed

    xls(x) -> pandas.core.frame.DataFrame

    arguments:
       filepath : string
       key : string
           -- the shared key of the file(s), which will appear in the merged
              excel file, default ['学号'].
       subkey : a list of string(s)
           -- the shared subkey of the file(s), which will not appear in the
           merged excel file, default []
    """
    filepath = str(filepath)
    df = pd.read_excel(filepath)
    df.index = range(len(df))

    for k in key+subkey:
        if k not in df.columns:
            l = key+subkey+[filepath]
            df = pd.read_excel(filepath,names=l)
            df[filepath] = df[filepath].fillna(1)
            break
    if len(df.columns) == len(key+subkey):
        df = DataFrame(df,columns=list(df.columns)+[filepath])
        df[filepath] = df[filepath].fillna(1)
    for i,j in zip(key,keyformat):
        df[i] = df[i].apply(lambda x:__stdiz__(x,j))

    for i in subkey:
        del df[i]
    return df


def join_list(lpath,key=['学号','姓名'],keyformat=['int','str'],subkey=[],
              inputfolder="input\\"):
    """
    process a list of xls(x) files and merge them into a new xls file

    arguments:
       lpath : list of string(s)
       out : string -- the name of the output file
    """
    
    
    d = __read__(str(inputfolder)+str(lpath[0]),key=key,subkey=subkey)
    for i in lpath[1:]:
        d = pd.merge(d,__read__(str(inputfolder)+str(i),key=key,keyformat=keyformat,
                                subkey=subkey),on=key,how='outer')
    return d


def to_excel(df,filename="output.xls",key=["姓名","学号"]):
    out = str(filename)
    if out[-4:] not in ['.xls','xlsx']:
        out = out + '.xls'
    if not os.path.exists("output\\"):
        os.mkdir("output\\")
    df.sort_index(by=key).to_excel("output\\"+out,index=False)
    return


def merge_to_metal(df,metdata="metal_data\\metal.xlsx",how='left',
                   key=['学号','姓名'],keyformat=['int','str'],subkey=[]):

    mt = pd.read_excel(metdata,names=key+subkey)
    for i,j in zip(key,keyformat):
        mt[i] = mt[i].apply(lambda x:__stdiz__(x,j))
    for i in subkey:
        del mt[i]
    return pd.merge(mt,df,how=how,on=key)


def total_process(lpath,key=['学号','姓名'],keyformat=['int','str'],subkey=[],
                  metdata="metal_data\\metal.xlsx",output="output.xls",
                  match=False,inputfolder="input\\"):
    lp = list(lpath)
    k = list(key)
    kf = list(keyformat)
    sk = list(subkey)
    mt = str(metdata)
    op = str(output)
    ip = str(inputfolder)
    
    df = join_list(lp,key=k,keyformat=kf,subkey=sk,inputfolder=ip)
    df = merge_to_metal(df,metdata=mt,how=('left' if match else 'outer'),
                        key=k,keyformat=kf,subkey=sk)
    to_excel(df,filename=op,key=k)
