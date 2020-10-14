# coding=utf-8
import os, sys, gc, datetime
from ICR2011.lib import *

pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None 



sys.path.append(file_dir)
os.chdir(file_dir)

rc = readfile("VC_ICA_RC_V_ICA_RC_T_46S.TXT")
newdata = rc[["I_RCODE", "I_AA_CLASS", "I_AUTO_TRIGGER", "I_DESCM_EN","I_EXACT_MATCH", "I_OUTPUT_STRUC", "I_REQUIRE_COMMENT","I_TEMPORAL","I_TEMP_FOR_NP","I_TRIGGER_PARTNER_SIDE","I_WF_SCENARIO_ID"]]
newdata = newdata.sort_values("I_RCODE")
newdata.rename(columns = dicts, inplace = True)
write_dir = "C:/dev/2011/40Y/"
newdata.to_csv(write_dir + "ReasonCode.csv",sep = ",", index = False, header= True)
write_dir = "C:/dev/2011/1SG/"
newdata.to_csv(write_dir + "ReasonCode.csv",sep = ",", index = False, header= True)