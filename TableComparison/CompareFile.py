# coding=gbk
import os
import os.path
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import datetime
import gc
import string as str
from TableComparison.lib import *



filelist = pd.read_csv(rootdir + "fincs_ecatt.TXT", sep = '\t',encoding='utf-16')


for i in range(filelist.shape[0]):
    file1 = target + filelist["ZTABLE"][i] + "_src1.csv"
    file2 = target + filelist["ZTABLE"][i] + "_src2.csv"
    if (os.path.isfile(file1) and os.path.isfile(file2)):
        df1 = pd.read_csv(file1, header = None)
        df2 = pd.read_csv(file2, header = None)
        filelist["ZFILE"][i] = df1.equals(df2)
    else:
        filelist["ZFILE"][i] = 'EmptyTable'
    
filelist.to_csv(target + "result.csv", sep = ',', index = False)  

