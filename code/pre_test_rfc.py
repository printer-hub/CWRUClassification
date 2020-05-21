# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:02:53 2020

@author: 23826
"""

import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
import joblib

#预测三次，三个model对对应的三个特征处理文件进行预测，输出三份预测文件

#test=pd.read_csv('../feature/test/test_selected_t_f.csv')#时域、频域

#test=pd.read_csv('../feature/test/test_selected_wt.csv')# 时域、频域

test=pd.read_csv('../feature/test/test_selected_all.csv')# 时域、频域、时频域


test_np=np.array(test)
test_x=np.float32(test_np[:,:-2])
test_filename=pd.DataFrame(test_np[:,-1],columns=['filename'])


#rfc =joblib.load('../model/rfc_t_f_model.model')# 时域、频域

#rfc =joblib.load('../model/rfc_wt_model.model') # 时频域
rfc =joblib.load('../model/rfc_all_model.model')# 时域、频域、时频域


test_pre=rfc.predict(test_x)
test_pre=pd.DataFrame(test_pre,columns=['label'])
test_out=pd.concat([test_pre,test_filename],axis=1)


#test_out.to_csv('../result/result1.csv',index=False)
#test_out.to_csv('../result/result2.csv',index=False)
test_out.to_csv('../result/result3.csv',index=False)


#之后再调用selectpre.py对三份预测文件进行整合



