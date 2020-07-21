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

rootdir = "C:/Users/i038196/Desktop/Comparison/"
filedir = rootdir + "HC6.715/"
filedir2 = rootdir + "HXF.803/"
target = rootdir + "target/"


def cleanfile(folder, filename):
    df = pd.read_csv(folder + filename, sep = '\t', header = None, encoding='utf-16')
    df = df.iloc[:,1:]
    df.to_csv(target + filename[0:-4] + "_src1.csv", sep = ',', header = None, index = False)
    
for root, dirs, files in os.walk(filedir):
    index = 0
    for file in files:
        cleanfile(filedir, file)

for root, dirs, files in os.walk(filedir2):
    index = 0
    for file in files:
        cleanfile(filedir2, file)
        

