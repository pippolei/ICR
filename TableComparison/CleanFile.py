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




def cleanfile(folder, filename):
    df = pd.read_excel(folder + filename)
    df.drop("MANDT", axis = 1, inplace = True)  #去掉client
    if(df.columns.contains("LANGU")):
        df = df[df["LANGU"] == 'E']
    df = df.sort_values(df.columns.to_list())
    df.to_csv(target + filename[0:-4] + "_src1.csv", sep = ',', index = False)
    
for root, dirs, files in os.walk(filedir):
    index = 0
    for file in files:
        cleanfile(filedir, file)

for root, dirs, files in os.walk(filedir2):
    index = 0
    for file in files:
        cleanfile(filedir2, file)
        

