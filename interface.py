print("Now initializing ... please wait ...")
import sys, os
sys.path.append('xls_pack.py')
from xls_pack import *
import pandas as pd

def fetchfiles(folder="\\input"):
    print("Now fetching excel files in the directory \"%s"%folder)
    l = pd.Series(os.listdir(os.getcwd()+folder))
    l = l[l.apply(lambda x: True if (str(x)[-4:]=='.xls' or str(x)[-4:]=='xlsx')
                  else False)]
    print("The files to be merged are below:")
    print(l)
    print("\n\n")
    return l
    
def main1(l):
    print("Step 1: Merge with \"姓名\",\"学号\" columns.\n")
    total_process(l,output="排重表格")
    print("Succeeded!\n\n")


def main2(l):
    print("Step 2: Merge with \"学号\",\"姓名\" columns.\n")
    total_process(l,key=['学号','姓名'],keyformat=['int'],subkey=[],match=True,output="整合表格")
    print("Succeeded!\n\n")


def main():
    l = fetchfiles()
    allclr = True
    
    k = find_duplicated(l)
    if(len(k)>0):
        if(allclr): 
            print("There are some duplicated data below:\n")
            allclr = False
        print(k,'\n')
    if(allclr):
        print("No duplicated data found.")
    else:
        print("Continue?(press q to quit):",end="")
        if(str(input())=='q'): return
    main2(l)
    os.system("pause")

main()
