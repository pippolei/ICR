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

file_dir = "C:/perforce/bp/Variant_Administration/Files/Suite_NW_760/sSuite_100/Central/Model_S"
write_dir = "C:/dev/40Y/"



dicts = {
    'I_RCODE':'Reason Code', 
    "I_AA_CLASS":'Adjustment Class', 
    "I_DESCM_EN":"Description",
    "I_AUTO_TRIGGER":'Automatically trigger follow-ups',
    "I_EXACT_MATCH":'Exact Match',
    "I_OUTPUT_STRUC":'Output Structure',
    "I_REQUIRE_COMMENT":'Comment Required',
    "I_TEMPORAL":'Temporary Resolution',
    "I_TEMP_FOR_NP":'Rematch in Next Period',
    "I_TRIGGER_PARTNER_SIDE":'Trigger on partner unit side',
    "I_WF_SCENARIO_ID":'Workflow Scenario',
    'I_METHOD_ID':'Method',
    'I_DESCL_EN':'Description',
    'I_DS_NAME':'DataSource Name',
    'I_LOW':'Value From',
    'I_HIGH':'Value To',
    'I_SELOPT':"Operator",
    'I_EXPR_ID':'Expression',
    'I_RULE_ID':'Rule',
    'I_COMPARATOR':'Operator',
    'I_FLDNM':'Field Name',
    'I_FLDNM1':'Field Name1',
    'I_FLDNM2':'Field Name2',
    'I_FIELD_NAME':'Field Name', 
    'I_G_FIELD_NAME': 'Field Name',
    'I_FIELD_LABEL_EN': "Label",
    'I_FUNCTION1':'Func1',
    'I_FUNCTION2':'Func2',
    'I_PARAMETER1':'Parameter1',
    'I_PARAMETER2':'Parameter2',
    'I_PARAMETERC':'Function Parameter',
    'I_GROUP_ON_SLICE1':'Group on slice1',
    'I_GROUP_ON_SLICE2':'Group on slice2',
    'I_IS_AGGR1':'Aggregation1',
    'I_IS_AGGR2':'Aggregation2',
    'I_MATCH_TYPE':'Match Type',
    'I_DS_NAME':"DataSource",
    'I_CDS_NAME':"CDS Name",
    'I_LUNIT_AO':'Authorization Object',
    'I_LUNIT_C_FIELD':'Leading Unit Superordinate Field',
    'I_LUNIT_ENTITY_CDS':'Unit Entity CDS View',
    'I_LUNIT_FIELD':'Leading Unit Field',
    'I_LUNIT_ENTITY_CDS':'Unit Entity CDS View',
    'I_PUNIT_C_FIELD':'Partner Unit Superordinate Field',
    "I_PUNIT_FIELD": "Partner Unit Field",
    'I_CONV_PROFILE_ID':'Profile ID',
    'I_CONV_TYPE':'Conversion Type',
    'I_DERIVE_TCURR':'Use Derived Target Currency',
    'I_EXCH_RATE_TYPE':'Exchange Rate Type',
    'I_GDATU_FIELD':'Reference Date',
    'I_TCURR':'Target Currency',
    'I_TUNIT':'Target Unit',
    'I_OBJECT_KEY':'Key',
    'I_SEARCH_HELP':'Search Help',
    'I_UPDATE_FLD':'Update from Original Doc',
    'I_DEFAULT_VALUE':'Default Value',
    'I_HIDE_FLD':'Hide from UI',
    'I_NAV_ID':'Nav ID',
    'I_NEW_BROWSER':'New Browser',
    'I_TARGET_URL':'Target URL',
    'I_URL_PARA':'URL Parameter',
    'I_URL_PARA_VALUE':'Param Value',
    'I_DC_NAME':'Posting Rule',
    'I_FIELD_VALUE':'Field Value',
    'I_ITEM_GROUP':'Item Group',
    'I_GROUP_STR':'Group-By String',
    'I_FLD_FUNC':'Field Function',
    'I_PARAM_VALUE':'Parameter Value',
    'I_RECON_CASE_ID':'ReconCase ID',
    'I_SAME_FYV':'With Balance Carryforward',
    'I_DESCL_EN_x':'Description',
    'I_DESCL_EN_y':'Description',
    'I_DESCL_EN_x':'Description',
    'I_DESCL_EN_y':'Description',
    'I_DISP_GROUP':'Display Group',
    'I_LEADING_GROUP':'Is Leading',
    'I_PAIRED_DISP_GROUP':'Paired Group',
    'I_AMNT_FIELD':'Measure Field',
    'I_CURR_FIELD':'Currency/Unit',
    'I_LEADING_AMNT':'Is Leading Measure',
    'I_SAME_SIGN':"Same Sign",
    'I_TOLERANCE_A':'Tolerance Amount',    
    'I_TOLERANCE_P':'Tolerance Percentage',
    'I_FILTER_ID':'Filter ID',
    'test2':31,
    'test2':31
    }
    
def clean(newdata):
    newdata = newdata.fillna("")
    newdata = newdata.replace(np.nan,"", regex = True).replace(np.NaN,"", regex=True)
    newdata.drop(['[VARIANT]', '[DESCRIPTION]'], axis = 1, inplace = True)
    newdata.drop(newdata.index[0], inplace = True)
    newdata.drop(newdata.index[0], inplace = True)
    return newdata
    
def readfile(filename):
    newdata = clean(pd.read_csv(filename, sep='\t', encoding='utf-16'))
    return newdata


def replaceColName(newdata):
    colname = newdata