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



dc = readfile("ICAD_ICA_DC_46S.TXT")
dc2 = readfile("ICAD_ICA_DC_4WE.TXT")
frame = [dc, dc2]
newdc = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ
newdc = newdc[["I_DC_NAME"]]


dct = readfile("ICAD_ICA_DCT_46S.TXT")
dct2 = readfile("ICAD_ICA_DCT_4WE.TXT")
frame = [dct, dct2]
newdct = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ
newdct = newdct[["I_DC_NAME","I_DESCL_EN"]]

dc_c = readfile("ICAD_ICA_DC_C_46S.TXT")
dc_c2 = readfile("ICAD_ICA_DC_C_4WE.TXT")
frame = [dc_c, dc_c2]
newdc_c = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ
#newdc_c = newdc_c.pivot("I_DC_NAME","I_FIELD_NAME","I_FIELD_VALUE")
#newdc_c.columns = "c_" + newdc_c.columns



dc_h = readfile("ICAD_ICA_DC_H_46S.TXT")
dc_h2 = readfile("ICAD_ICA_DC_H_4WE.TXT")
frame = [dc_h, dc_h2]
newdc_h = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ
#newdc_h = newdc_h.pivot("I_DC_NAME","I_FIELD_NAME","I_FIELD_VALUE")
#newdc_h.columns = "h_" + newdc_h.columns
frame = [newdc_c, newdc_h]
newdc = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ


dc_ig = readfile("ICAD_ICA_DC_IG_46S.TXT")
dc_ig2 = readfile("ICAD_ICA_DC_IG_4WE.TXT")
frame = [dc_ig, dc_ig2]
newdc_ig = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ
newdc_ig.drop(["I_LOOP_OPTION"], axis = 1, inplace = True)

dc_igf = readfile("ICAD_ICA_DC_IG_FLD_46S.TXT")
dc_igf2 = readfile("ICAD_ICA_DC_IG_FLD_4WE.TXT")
frame = [dc_igf, dc_igf2]
newdc_igf = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ
newdc_igf.drop(["I_RULE_UUID","I_PREV_RULE_ID"], axis = 1, inplace = True)
newdc_ig = pd.merge(newdc_ig,newdc_igf, on = ["I_DC_NAME", "I_ITEM_GROUP"])
newdc_ig.drop(["I_GROUP_STR_EXT1","I_GROUP_STR_EXT2","I_GROUP_STR_EXT3"], axis = 1, inplace = True)

newdata = pd.merge(newdct, newdc, on = ['I_DC_NAME'])
newdata = newdata.replace(np.NaN, "", regex = True)

newdata.rename(columns = dicts, inplace = True)

newdc_ig.rename(columns = dicts, inplace = True)
newdata.to_csv(write_dir + "PostingRule_header.csv",sep = ",", index = False, header= True)
newdc_ig.to_csv(write_dir + "PostingRule_item.csv",sep = ",", index = False, header= True)

