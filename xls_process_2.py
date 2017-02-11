"""

A package to process minor problems in EXCEL documents of student
attendences in Nanjing Medical University                --by Xie

MAKE SURE YOU HAVE INSTALLED 'PANDAS' BEFORE YOU USE THIS PACKAGE!!!
"""

import os
import pandas as pd
import numpy as np
from pandas import DataFrame, Series

def __stdstno__(stno):
    if type(stno)==str:
        x = stno.strip()
        if x[0]=="'":
           return int(x[1:])
        return int(x)
    else:
        return stno

def __stdname__(stn):
    return stn

def __read__(filepath,key='学号',subkey='姓名'):
    """
    read a xls(x) file in filepath and return a pandas.DataFrame object
    with its column name processed

    xls(x) -> pandas.core.frame.DataFrame

    arguments:
       filepath : string
       key : string
           -- the shared key of the file(s), default '学号'
       subkey : a list of string(s)
           -- the shared subkey of the file(s), default '姓名'
    """
    filepath = str(filepath)
    df = pd.read_excel(filepath)
    df.index = range(len(df))

    if key not in df.columns:
        l = [key]+[subkey]+[filepath]
        for i in range(2,len(df.columns)-1):
            l.append(filepath+str(i))
        df = pd.read_excel(filepath,names=l)
    elif len(df.columns) == 2 and filepath!='main.xlsx': #to do : modify it to be less specialized
        df = DataFrame(df,columns=list(df.columns)+[filepath])
        df.fillna(1,inplace=True)
    df.学号 = df.学号.apply(__stdstno__)
    df.姓名 = df.姓名.apply(__stdname__)
    return df

def process_args(path, *args,out="output.xls"):
    """
    process a list of xls(x) files and merge them into a new xls file

    arguments:
       path : string(s)
       out : string -- the name of the output file
    """
    out = str(out)
    if out[-4:] not in ['.xls','xlsx']:
        out = out + '.xls'
    
    d = __read__(str(path))
    for i in args:
        d = pd.merge(d,__read__(str(i)),how='outer')
    d.to_excel(out,index=False)
    return

def process_list(lpath,out="output.xls",on=['学号','姓名']):
    """
    process a list of xls(x) files and merge them into a new xls file

    arguments:
       lpath : list of string(s)
       out : string -- the name of the output file
    """
    out = str(out)
    if out[-4:] not in ['.xls','xlsx']:
        out = out + '.xls'
    if not os.path.exists("output\\"):
        os.mkdir("output\\")
    
    
    d = __read__(lpath[0],key=on[0],subkey=on[1])
    for i in lpath[1:]:
        d = pd.merge(d,__read__(str(i),key=on[0],subkey=on[1]),on=on,how='outer')
    d.to_excel("output\\"+out,index=False)
    return
