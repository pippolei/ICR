# coding=utf-8
import os, sys, gc, datetime
from ICR2011.lib import *


pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None 


sys.path.append(file_dir)
os.chdir(file_dir)

method = readfile("ICAM_ICA_METHOD_46S.TXT")
method2 = readfile("ICAM_ICA_METHOD_4WE.TXT")

methodt = readfile("ICAM_ICA_METHODT_46S.TXT")
methodt2 = readfile("ICAM_ICA_METHODT_4WE.TXT")

method_ds = readfile("ICAM_ICA_METHOD_DS_46S.TXT")
method_ds2 = readfile("ICAM_ICA_METHOD_DS_4WE.TXT")

method_expr = readfile("ICAM_ICA_METHOD_EXPR_46S.TXT")
method_expr2 = readfile("ICAM_ICA_METHOD_EXPR_4WE.TXT")

method_fltr = readfile("ICAM_ICA_METHOD_FLTR_46S.TXT")
method_fltr2 = readfile("ICAM_ICA_METHOD_FLTR_4WE.TXT")

method_rule = readfile("ICAM_ICA_METHOD_RULE_46S.TXT")
method_rule2 = readfile("ICAM_ICA_METHOD_RULE_4WE.TXT")

method_rulet = readfile("ICAM_ICA_METHOD_RULET_46S.TXT")
method_rulet2 = readfile("ICAM_ICA_METHOD_RULET_4WE.TXT")

def generateMatchingMethod(method, methodt, method_ds,method_expr, method_fltr, method_rule, method_rulet, write_dir):
    method = method[["I_METHOD_ID"]]
    methodt = methodt[["I_METHOD_ID","I_DESCL_EN"]]
    method_ds = method_ds[["I_DS_NAME","I_METHOD_ID"]]

    method_fltr["I_DS_NAME"] = method_fltr["I_FILTER_ID"]
    method_fltr["I_RULE_ID"] = "#" + method_fltr["I_FILTER_ID"].apply(lambda x: x.split("#")[0]) 

    method_rule.drop(["I_INACTIVE","I_SLICE1_FILTER_STR","I_SLICE2_FILTER_STR","I_SLICE2","I_SLICE1","I_SLICE1_POSIT_NO","I_SLICE2_POSIT_NO"], axis = 1, inplace = True)
    
    method_rulet = method_rulet[["I_METHOD_ID","I_RULE_ID","I_DESCM_EN"]]

    newdata = pd.merge(method, methodt, on = ['I_METHOD_ID'])
    newdata = pd.merge(newdata, method_ds, on = ['I_METHOD_ID'])
    newdata = pd.merge(newdata, method_fltr, on = ['I_METHOD_ID','I_DS_NAME'])

    ruledata = pd.merge(method_rule, method_rulet, on = ['I_METHOD_ID','I_RULE_ID'])
    ruledata = pd.merge(ruledata, method_fltr, on = ['I_METHOD_ID','I_RULE_ID'])
    ruledata.drop(["I_POSIT_NO","I_SIGN","I_PREV_RULE_ID"], axis = 1, inplace = True)

    newdata.drop(["I_FILTER_ID", "I_RULE_ID", "I_POSIT_NO", "I_SIGN"], axis = 1, inplace = True)
    newdata = newdata[['I_METHOD_ID', 'I_DESCL_EN', 'I_DS_NAME', 'I_FLDNM', 'I_SELOPT', 'I_LOW', 'I_HIGH']]
    newdata.rename(columns = dicts, inplace = True)
    newdata.to_csv(write_dir + "MatchingMethod_Header.csv",sep = ",", index = False, header= True)
    ruledata.drop(["I_FILTER_ID", "I_DS_NAME"], axis = 1, inplace = True)
    ruledata = ruledata.sort_values(["I_METHOD_ID","I_RULE_ID"])
    ruledata.rename(columns = dicts, inplace = True)
    ruledata.to_csv(write_dir + "MatchingMethod_Rule_Filter.csv",sep = ",", index = False, header= True)
    method_expr = pd.merge(method_expr, method_rulet, on = ['I_METHOD_ID', 'I_RULE_ID'])
    method_expr = method_expr.sort_values(["I_METHOD_ID","I_RULE_ID","I_EXPR_ID"])
    method_expr.rename(columns = dicts, inplace = True)
    method_expr.to_csv(write_dir + "MatchingMethod_Rule_Expression.csv",sep = ",", index = False, header= True)



write_dir = "C:/dev/2011/40Y/"
generateMatchingMethod(method, methodt, method_ds,method_expr, method_fltr, method_rule, method_rulet, write_dir)
write_dir = "C:/dev/2011/1SG/"
generateMatchingMethod(method2, methodt2, method_ds2,method_expr2, method_fltr2, method_rule2, method_rulet2, write_dir)












