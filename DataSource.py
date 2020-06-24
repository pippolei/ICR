# coding=utf-8
import os, sys, gc, datetime
import matplotlib
import numpy as np
import pandas as pd
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
import xlsxwriter

pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None 



sys.path.append(file_dir)
os.chdir(file_dir)



ds = readfile("VC_ICA_DS_V_ICA_DS_T_46S.TXT")
ds2 = readfile("VC_ICA_DS_V_ICA_DS_T_4WE.TXT")
frame = [ds, ds2]
newds = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ0
newds = newds[["I_DS_NAME", "I_CDS_NAME","I_DESCL_EN", "I_LUNIT_AO", "I_LUNIT_C_FIELD", "I_LUNIT_ENTITY_CDS", "I_LUNIT_FIELD", "I_PUNIT_C_FIELD", "I_PUNIT_FIELD"]]

ds_filter = readfile("VC_ICA_DS_V_ICA_DS_MFF_46S.TXT")
ds_filter2 = readfile("VC_ICA_DS_V_ICA_DS_MFF_4WE.TXT")
frame = [ds_filter, ds_filter2]
new_ds_filter = pd.concat(frame, axis = 0, sort = False) 

ds_nav = readfile("VC_ICA_DS_V_ICA_DS_NAV_T_46S.TXT")
ds_nav2 = readfile("VC_ICA_DS_V_ICA_DS_NAV_T_4WE.TXT")
frame = [ds_nav, ds_nav2]
new_ds_nav = pd.concat(frame, axis = 0, sort = False) 
new_ds_nav = new_ds_nav[["I_DS_NAME", "I_FIELD_NAME","I_NAV_ID", "I_DESCM_EN", "I_NEW_BROWSER", "I_TARGET_URL"]]

ds_param = readfile("VC_ICA_DS_V_ICA_DS_PARA_46S.TXT")
ds_param2 = readfile("VC_ICA_DS_V_ICA_DS_PARA_4WE.TXT")
frame = [ds_param, ds_param2]
new_ds_param = pd.concat(frame, axis = 0, sort = False) 
new_ds_nav2 = pd.merge(new_ds_nav, new_ds_param, on = ['I_DS_NAME','I_FIELD_NAME','I_NAV_ID'])


ds_conv = readfile("VC_ICA_DS_V_ICA_DS_CP_T_46S.TXT")
ds_conv2 = readfile("VC_ICA_DS_V_ICA_DS_CP_T_4WE.TXT")
frame = [ds_conv, ds_conv2]
new_ds_conv = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ0
new_ds_conv = new_ds_conv[["I_CONV_PROFILE_ID","I_DS_NAME","I_CONV_TYPE","I_DERIVE_TCURR","I_DESCL_EN","I_EXCH_RATE_TYPE","I_GDATU_FIELD","I_TCURR","I_TUNIT"]]

ds_field = readfile("VC_ICA_DS_V_ICA_DS_FS_T_46S.TXT")
ds_field2 = readfile("VC_ICA_DS_V_ICA_DS_FS_T_4WE.TXT")
frame = [ds_field, ds_field2]
new_ds_field = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ0
new_ds_field = new_ds_field[["I_DS_NAME","I_FIELD_NAME","I_FIELD_LABEL_EN","I_G_FIELD_NAME","I_OBJECT_KEY","I_SEARCH_HELP","I_UPDATE_FLD"]]



newdata_filter = pd.merge(newds, new_ds_filter, on = ['I_DS_NAME'])
newdata_nav = pd.merge(newds, new_ds_nav2, on = ['I_DS_NAME'])
newdata_conversion = pd.merge(newds, new_ds_conv, on = ['I_DS_NAME'])

newdata_filter.rename(columns = dicts, inplace = True)
newdata_nav.rename(columns = dicts, inplace = True)
newdata_conversion.rename(columns = dicts, inplace = True)
new_ds_field = new_ds_field.sort_values(["I_DS_NAME","I_FIELD_NAME"])
new_ds_field.rename(columns = dicts, inplace = True)

newdata_filter.to_csv(write_dir + "DataSource_FilterFields.csv",sep = ",", index = False, header= True)
newdata_nav.to_csv(write_dir + "DataSource_NavigationSetting.csv",sep = ",", index = False, header= True)
newdata_conversion.to_csv(write_dir + "DataSource_ConversionProfile.csv",sep = ",", index = False, header= True)
new_ds_field.to_csv(write_dir + "DataSource_FieldSemantics.csv",sep = ",", index = False, header= True)

