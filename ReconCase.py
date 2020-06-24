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



sys.path.append(file_dir)
os.chdir(file_dir)

rc = readfile("ICAC_ICA_RECON_CASE_46S.TXT")
rc2 = readfile("ICAC_ICA_RECON_CASE_4WE.TXT")

frame = [rc, rc2]
newrc = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ0
newrc = newrc[["I_RECON_CASE_ID","I_METHOD_ID","I_SAME_FYV"]]

rct = readfile("ICAC_ICA_RECON_CASET_46S.TXT")
rct2 = readfile("ICAC_ICA_RECON_CASET_4WE.TXT")
frame = [rct, rct2]
newrct = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ0
newrct = newrct[["I_RECON_CASE_ID","I_DESCL_EN"]]
newrc = pd.merge(newrc, newrct, on = ['I_RECON_CASE_ID'])

rc_dg = readfile("ICAC_ICA_RECON_DG_46S.TXT")
rc_dg2 = readfile("ICAC_ICA_RECON_DG_4WE.TXT")
frame = [rc_dg, rc_dg2]
newrc_dg = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ0

rc_dgt = readfile("ICAC_ICA_RECON_DGT_46S.TXT")
rc_dgt2 = readfile("ICAC_ICA_RECON_DGT_4WE.TXT")
frame = [rc_dgt, rc_dgt2]
newrc_dgt = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ0
newrc_dgt = newrc_dgt[["I_DISP_GROUP","I_RECON_CASE_ID","I_DESCL_EN"]]
newrc_dgt["I_DESCL_EN"] = newrc_dgt["I_DESCL_EN"].apply(lambda x: x.replace("-", ""))
newrc_dg = pd.merge(newrc_dg, newrc_dgt, on = ['I_RECON_CASE_ID','I_DISP_GROUP'])

rc_filt = readfile("ICAC_ICA_RECON_FLTR_46S.TXT")
rc_filt2 = readfile("ICAC_ICA_RECON_FLTR_4WE.TXT")
frame = [rc_filt, rc_filt2]
newrc_filter = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ0
#newrc_filter.drop(["I_IS_VIRTUAL","I_TOLERANCE_Q","I_IS_QUANTITY"], axis = 1, inplace = True)

rc_tol = readfile("ICAC_ICA_RECON_TOL_46S.TXT")
rc_tol2 = readfile("ICAC_ICA_RECON_TOL_4WE.TXT")
frame = [rc_tol, rc_tol2]
newrc_tol = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ0
newrc_tol = newrc_tol[["I_AMNT_FIELD","I_DISP_GROUP","I_RECON_CASE_ID","I_CURR_FIELD","I_LEADING_AMNT","I_SAME_SIGN","I_TOLERANCE_A","I_TOLERANCE_P"]]


rc_tolv = readfile("ICAC_ICA_RECON_TOLV_46S.TXT")
rc_tolv2 = readfile("ICAC_ICA_RECON_TOLV_4WE.TXT")
frame = [rc_tolv, rc_tolv2]
newrc_tolv = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ0

rc_tolvt = readfile("ICAC_ICA_RECON_TOLVT_46S.TXT")
rc_tolvt2 = readfile("ICAC_ICA_RECON_TOLVT_4WE.TXT")
frame = [rc_tolvt, rc_tolvt2]
newrc_tolvt = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ0

newdata = pd.merge(newrc, newrc_dg, on = ['I_RECON_CASE_ID'])
newdata = pd.merge(newdata, newrc_tol, on = ['I_RECON_CASE_ID',"I_DISP_GROUP"])

newdata.rename(columns = dicts, inplace = True)
newrc_filter.drop(['I_SIGN'], axis = 1, inplace = True)
newrc_filter.rename(columns = dicts, inplace = True)
newdata.to_csv(write_dir + "ReconCase.csv",sep = ",", index = False, header= True)
newrc_filter.to_csv(write_dir + "ReconCase_Filter.csv",sep = ",", index = False, header= True)