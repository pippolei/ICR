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
import lib

pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None 

file_dir = "C:/dev/40Y"

sys.path.append(file_dir)
os.chdir(file_dir)



ds = lib.clean(pd.read_csv("VC_ICA_DS_V_ICA_DS_T_46S.TXT", sep='\t'))
ds2 = lib.clean(pd.read_csv("VC_ICA_DS_V_ICA_DS_T_4WE.TXT", sep='\t'))
frame = [ds, ds2]
newds = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ0
newds = newds[["I_DS_NAME", "I_CDS_NAME","I_DESCL_EN", "I_LUNIT_AO", "I_LUNIT_C_FIELD", "I_LUNIT_ENTITY_CDS", "I_LUNIT_FIELD"]]

ds_filter = lib.clean(pd.read_csv("VC_ICA_DS_V_ICA_DS_MFF_46S.TXT", sep='\t'))
ds_filter2 = lib.clean(pd.read_csv("VC_ICA_DS_V_ICA_DS_MFF_4WE.TXT", sep='\t'))
frame = [ds_filter, ds_filter2]
new_ds_filter = pd.concat(frame, axis = 0, sort = False) 

ds_nav = lib.clean(pd.read_csv("VC_ICA_DS_V_ICA_DS_NAV_T_46S.TXT", sep='\t'))
ds_nav2 = lib.clean(pd.read_csv("VC_ICA_DS_V_ICA_DS_NAV_T_4WE.TXT", sep='\t'))
frame = [ds_nav, ds_nav2]
new_ds_nav = pd.concat(frame, axis = 0, sort = False) 
new_ds_nav = new_ds_nav[["I_DS_NAME", "I_FIELD_NAME","I_NAV_ID", "I_DESCM_EN", "I_NEW_BROWSER", "I_TARGET_URL"]]

ds_param = lib.clean(pd.read_csv("VC_ICA_DS_V_ICA_DS_PARA_46S.TXT", sep='\t'))
ds_param2 = lib.clean(pd.read_csv("VC_ICA_DS_V_ICA_DS_PARA_4WE.TXT", sep='\t'))
frame = [ds_param, ds_param2]
new_ds_param = pd.concat(frame, axis = 0, sort = False) 
new_ds_nav2 = pd.merge(new_ds_nav, new_ds_param, on = ['I_DS_NAME','I_FIELD_NAME','I_NAV_ID'])


ds_conv = lib.clean(pd.read_csv("VC_ICA_DS_V_ICA_DS_CP_T_46S.TXT", sep='\t'))
ds_conv2 = lib.clean(pd.read_csv("VC_ICA_DS_V_ICA_DS_CP_T_4WE.TXT", sep='\t'))
frame = [ds_conv, ds_conv2]
new_ds_conv = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ0
new_ds_conv = new_ds_conv[["I_CONV_PROFILE_ID","I_DS_NAME","I_CONV_TYPE","I_DERIVE_TCURR","I_DESCL_EN","I_EXCH_RATE_TYPE","I_GDATU_FIELD","I_TCURR","I_TUNIT"]]

ds_field = lib.clean(pd.read_csv("VC_ICA_DS_V_ICA_DS_FS_T_46S.TXT", sep='\t'))
ds_field2 = lib.clean(pd.read_csv("VC_ICA_DS_V_ICA_DS_FS_T_4WE.TXT", sep='\t'))
frame = [ds_field, ds_field2]
new_ds_field = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ0
new_ds_field = new_ds_field[["I_DS_NAME","I_FIELD_NAME","I_FIELD_LABEL_EN","I_G_FIELD_NAME","I_OBJECT_KEY","I_SEARCH_HELP","I_UPDATE_FLD"]]



newdata_filter = pd.merge(newds, new_ds_filter, on = ['I_DS_NAME'])
newdata_nav = pd.merge(newds, new_ds_nav2, on = ['I_DS_NAME'])
newdata_conversion = pd.merge(newds, new_ds_conv, on = ['I_DS_NAME'])


newdata_filter.to_csv("ds_filter.csv",sep = ",", index = False, header= True)
newdata_nav.to_csv("ds_naviation.csv",sep = ",", index = False, header= True)
newdata_conversion.to_csv("ds_conversion.csv",sep = ",", index = False, header= True)
new_ds_field.to_csv("ds_field.csv",sep = ",", index = False, header= True)
