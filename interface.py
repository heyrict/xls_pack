print("-"*50+"\n")
print("A program designed to find duplicated data and merge data in")
print("several excel files.\n")
print("More details in Github: http://github.com/heyrict/xls_pack")
print("\n"+"-"*50)
print("\n\n")
print(">>>Now initializing ... please wait ...")
import sys, os
sys.path.append('xls_pack.py')
from xls_pack import *
import pandas as pd

def fetchfiles(folder="\\input"):
    print(">>>Now fetching excel files in the directory \"%s\""%folder)
    l = pd.Series(os.listdir(os.getcwd()+folder))
    l = l[l.apply(lambda x: True if (str(x)[-4:]=='.xls' or str(x)[-4:]=='xlsx')
                  else False)]
    return l


def main2(l):
    print(">>>Now Merging with \"学号\",\"姓名\" columns.\n")
    total_process(l,key=['学号','姓名'],keyformat=['int','str'],subkey=[],match=True,output="整合表格")
    print(">>>Succeeded!\n\n")


def main():
    first_use = False
    if not os.path.exists("input\\"):
        os.mkdir("input\\")
        open("input\\PLACE INPUT FILES HERE","w").close()
        first_use = True
    if not os.path.exists("meta_data\\"):
        os.mkdir("meta_data\\")
        first_use = True
    if not os.path.exists("meta_data\\meta.xlsx"):
        open("meta_data\\meta.xlsx","w").close()
    if first_use:
        print(">>>Please put excel files that you want to merge in \"\\input\" folder")
        os.system("pause")
    elif os.path.getsize("meta_data\\meta.xlsx") == 0:
            print("WARNING: METADATA IS EMPTY!")

    l = fetchfiles()

    if len(l)==0 :
        print(">>>ERROR: NO EXCEL FILES FOUND IN \"\\input\"")
        os.system("pause")
        return
    
    print(">>>The files to be merged are below:")
    inputlist = list(l)
    for i in range(len(inputlist)):
        print(i+1,"  ",inputlist[i])
    print("\n\n")

    k = find_duplicated(l)
    if(type(k)==pd.DataFrame):
        print(">>>There are some duplicated data below:")
        allclr = False
        print(k,'\n')
    else:
        print(">>>No duplicated data found.")
    print(">>>Continue?(y/n):",end="")
    while(1):
        sig = str(input())
        if(sig=='n'): 
            os.system("pause")
            return
        elif(sig=='y'):
            break
        print(">>>Please input y or n:",end="")
    main2(l)
    os.system("pause")
    return

main()
