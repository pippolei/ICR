# coding=utf-8
import os, sys, gc, datetime
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder 
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb
import lightgbm as lgb
from xgboost import XGBClassifier
from sklearn.svm import SVC   
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from ICR2011.lib import *
import xlsxwriter


def WriteXlsx(write_dir):
    xlsx_writer = pd.ExcelWriter(write_dir + 'ICR_Configuration.xlsx', engine='xlsxwriter')
    for root, dirs, files in os.walk(write_dir):  
        for file in files:
                data = pd.read_csv(root + file, sep=',')
                data.to_excel(xlsx_writer, sheet_name=file.replace(".csv",""))
    

    xlsx_writer.save()
    
write_dir = "C:/dev/2011/40Y/"
WriteXlsx(write_dir)
write_dir = "C:/dev/2011/1SG/"
WriteXlsx(write_dir)