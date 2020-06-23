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
from lib import *

pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None 

file_dir = "C:/perforce/bp/Variant_Administration/Files/Suite_NW_760/sSuite_100/Central/Model_S"

sys.path.append(file_dir)
os.chdir(file_dir)

rc = readfile("VC_ICA_RC_V_ICA_RC_T_46S.TXT")
newdata = rc[["I_RCODE", "I_AA_CLASS", "I_AUTO_TRIGGER", "I_DESCM_EN","I_EXACT_MATCH", "I_OUTPUT_STRUC", "I_REQUIRE_COMMENT","I_TEMPORAL","I_TEMP_FOR_NP","I_TRIGGER_PARTNER_SIDE","I_WF_SCENARIO_ID"]]
newdata = newdata.sort_values("I_RCODE")
newdata.rename(columns = dicts, inplace = True)
newdata.to_csv("C:/dev/40Y/readoncode.csv",sep = ",", index = False, header= True)