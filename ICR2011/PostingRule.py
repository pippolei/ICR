# coding=utf-8
import os, sys, gc, datetime
from ICR2011.lib import *

pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None 



sys.path.append(file_dir)
os.chdir(file_dir)


dc = readfile("ICAD_ICA_DC_46S.TXT")
dc2 = readfile("ICAD_ICA_DC_4WE.TXT")

dct = readfile("ICAD_ICA_DCT_46S.TXT")
dct2 = readfile("ICAD_ICA_DCT_4WE.TXT")

dc_c = readfile("ICAD_ICA_DC_C_46S.TXT")
dc_c2 = readfile("ICAD_ICA_DC_C_4WE.TXT")

dc_h = readfile("ICAD_ICA_DC_H_46S.TXT")
dc_h2 = readfile("ICAD_ICA_DC_H_4WE.TXT")

dc_ig = readfile("ICAD_ICA_DC_IG_46S.TXT")
dc_ig2 = readfile("ICAD_ICA_DC_IG_4WE.TXT")

dc_igf = readfile("ICAD_ICA_DC_IG_FLD_46S.TXT")
dc_igf2 = readfile("ICAD_ICA_DC_IG_FLD_4WE.TXT")

def generatePostRule(dc, dct, dc_c, dc_h, dc_ig, dc_igf, write_dir):
    newdc = dc[["I_DC_NAME"]]
    newdct = dct[["I_DC_NAME","I_DESCL_EN"]]

    frame = [dc_c, dc_h]
    newdc = pd.concat(frame, axis = 0, sort = False) #�кϲ�, ��Ϊ
    newdc_ig = dc_ig.drop(["I_LOOP_OPTION"], axis = 1)

    newdc_igf = dc_igf.drop(["I_RULE_UUID","I_PREV_RULE_ID"], axis = 1)
    newdc_ig = pd.merge(newdc_ig,newdc_igf, on = ["I_DC_NAME", "I_ITEM_GROUP"])
    newdc_ig.drop(["I_GROUP_STR_EXT1","I_GROUP_STR_EXT2","I_GROUP_STR_EXT3"], axis = 1, inplace = True)

    newdata = pd.merge(newdct, newdc, on = ['I_DC_NAME'])
    newdata = newdata.replace(np.NaN, "", regex = True)

    newdata.rename(columns = dicts, inplace = True)
    newdc_ig.rename(columns = dicts, inplace = True)
    newdata.to_csv(write_dir + "PostingRule_header.csv",sep = ",", index = False, header= True)
    newdc_ig.to_csv(write_dir + "PostingRule_item.csv",sep = ",", index = False, header= True)

write_dir = "C:/dev/2011/40Y/"
generatePostRule(dc, dct, dc_c, dc_h, dc_ig, dc_igf, write_dir)
write_dir = "C:/dev/2011/1SG/"
generatePostRule(dc2, dct2, dc_c2, dc_h2, dc_ig2, dc_igf2, write_dir)










