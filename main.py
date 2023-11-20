#####
###
# 00 Imports
# 01 Pipelines
###
#####




#####
###
# 00 Imports
###
#####
from scripts.data_functions import *
from scripts.model_functions import *





#####
###
# 01 Pipelines
###
#####

# data pipeline
mf_train_df, mf_test_df, wm_train_df, wm_test_df = data_pipeline()

# model pipeline
mf_pred_df = model_pipeline(mf_train_df, mf_test_df)
wb_pred_df = model_pipeline(wm_train_df, wm_test_df)

# save data
mf_pred_df.to_csv('data/mf_pred_df.csv', index=False)
wb_pred_df.to_csv('data/wb_pred_df.csv', index=False)
