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
from ICR2011.lib import *
import xlsxwriter

pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None 

sys.path.append(file_dir)
os.chdir(file_dir)


ds = readfile("VC_ICA_DS_V_ICA_DS_T_46S.TXT")
ds2 = readfile("VC_ICA_DS_V_ICA_DS_T_4WE.TXT")

ds_filter = readfile("VC_ICA_DS_V_ICA_DS_MFF_46S.TXT")
ds_filter2 = readfile("VC_ICA_DS_V_ICA_DS_MFF_4WE.TXT")

ds_nav = readfile("VC_ICA_DS_V_ICA_DS_NAV_T_46S.TXT")
ds_nav2 = readfile("VC_ICA_DS_V_ICA_DS_NAV_T_4WE.TXT")

ds_param = readfile("VC_ICA_DS_V_ICA_DS_PARA_46S.TXT")
ds_param2 = readfile("VC_ICA_DS_V_ICA_DS_PARA_4WE.TXT")

ds_conv = readfile("VC_ICA_DS_V_ICA_DS_CP_T_46S.TXT")
ds_conv2 = readfile("VC_ICA_DS_V_ICA_DS_CP_T_4WE.TXT")

ds_field = readfile("VC_ICA_DS_V_ICA_DS_FS_T_46S.TXT")
ds_field2 = readfile("VC_ICA_DS_V_ICA_DS_FS_T_4WE.TXT")

def generateDS(ds, ds_filter, ds_nav, ds_param, ds_conv, ds_field, write_dir):
    newds = ds[["I_DS_NAME", "I_CDS_NAME", "I_DESCM_EN", "I_LUNIT_AO", "I_LUNIT_C_FIELD", "I_LUNIT_ENTITY_CDS", "I_LUNIT_FIELD", "I_PUNIT_C_FIELD", "I_PUNIT_FIELD","I_DESCL_EN"]]
    newds.rename(columns = dicts, inplace = True)
    newds.to_csv(write_dir + "DataSource_Header.csv",sep = ",", index = False, header= True)
    
    new_ds_nav = ds_nav[["I_DS_NAME", "I_FIELD_NAME","I_NAV_ID", "I_DESCM_EN", "I_NEW_BROWSER", "I_TARGET_URL"]]
    new_ds_nav2 = pd.merge(new_ds_nav, ds_param, on = ['I_DS_NAME','I_FIELD_NAME','I_NAV_ID'])

    new_ds_conv = ds_conv[["I_CONV_PROFILE_ID","I_DS_NAME","I_CONV_TYPE","I_DERIVE_TCURR","I_DESCL_EN","I_EXCH_RATE_TYPE","I_GDATU_FIELD","I_TCURR","I_TUNIT"]]

    new_ds_field = ds_field[["I_DS_NAME","I_FIELD_NAME","I_FIELD_LABEL_EN","I_G_FIELD_NAME","I_OBJECT_KEY","I_SEARCH_HELP","I_UPDATE_FLD"]]

    
    newdata_filter = ds_filter
    newdata_nav = new_ds_nav2
    newdata_conversion = new_ds_conv

    newdata_filter = newdata_filter.sort_values(["I_DS_NAME","I_FIELD_NAME"])
    newdata_filter.rename(columns = dicts, inplace = True)

    newdata_nav.rename(columns = dicts, inplace = True)
    newdata_conversion.rename(columns = dicts, inplace = True)

    new_ds_field = new_ds_field.sort_values(["I_DS_NAME","I_FIELD_NAME"])
    new_ds_field.rename(columns = dicts, inplace = True)

    newdata_filter.to_csv(write_dir + "DataSource_FilterFields.csv",sep = ",", index = False, header= True)
    newdata_nav.to_csv(write_dir + "DataSource_NavigationSetting.csv",sep = ",", index = False, header= True)
    newdata_conversion.to_csv(write_dir + "DataSource_ConversionProfile.csv",sep = ",", index = False, header= True)
    new_ds_field.to_csv(write_dir + "DataSource_FieldSemantics.csv",sep = ",", index = False, header= True)

write_dir = "C:/dev/2011/40Y/"
generateDS(ds, ds_filter, ds_nav, ds_param, ds_conv, ds_field, write_dir)
write_dir = "C:/dev/2011/1SG/"
generateDS(ds, ds_filter2, ds_nav2, ds_param2, ds_conv2, ds_field2, write_dir)











