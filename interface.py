import sys, os
sys.path.append('xls_process.py')
from xls_process_2 import *
import pandas as pd

print("Now fetching excel files in the current directory")
l = pd.Series(os.listdir(os.getcwd()))
l = l[l.apply(lambda x: True if (str(x)[-4:]=='.xls' or str(x)[-4:]=='xlsx')
              else False)]

print("The files to be merged are below:")
print(l)

process_list(list(l))

print("Succeeded!")
os.system("pause")
