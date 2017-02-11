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
    print("Succeeded!")


def main2(l):
    print("Step 2: Merge with \"学号\" column only.\n")
    total_process(l,key=['学号'],keyformat=['int'],subkey=['姓名'],match=True,output="整合表格")
    print("Succeeded!")


def main():
    l = fetchfiles()
    main1(l)
    main2(l)
    os.system("pause")

main()
