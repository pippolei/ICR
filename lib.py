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
from pip._vendor.pyparsing import Regex
pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None 

def clean(newdata):
    newdata = newdata.fillna("")
    newdata = newdata.replace(np.nan,"", regex = True).replace(np.NaN,"", regex=True)
    newdata.drop(['[VARIANT]', '[DESCRIPTION]'], axis = 1, inplace = True)
    newdata.drop(newdata.index[0], inplace = True)
    newdata.drop(newdata.index[0], inplace = True)
    return newdata
    