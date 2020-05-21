# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 08:51:01 2020

@author: 23826
"""
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train(train_data):
    # 模型初始化，设置random_state保证可复现性，便于观察优化
    #train_data = pd.read_csv('../feature/feature_select512.csv')
    train_data_y = train_data['label']
    # 除去标签的所有列就是特征
    train_data_x = train_data.drop(['label','RPM'], axis=1)
    model_rfc=RandomForestClassifier(random_state=0,n_estimators=100)
    # 模型训练
    model_rfc.fit(train_data_x, train_data_y)
    #保存模型
    joblib.dump(model_rfc, '../model/rfc_all_model.model')


train_data=pd.read_csv('../feature/train/train_selected_all.csv')
train_data_np =np.array(train_data)
X=train_data_np[:,0:-2]
Y=train_data_np[:,-1]
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.2, random_state=0)
rfc=RandomForestClassifier(random_state=0,n_estimators=100,oob_score=True)
# 模型训练
rfc.fit(train_X,train_Y)
pred_Y = rfc.predict(test_X)
acc=accuracy_score(test_Y,pred_Y)
#用所有样本训练并保存模型
train(train_data)
#test_lightgbm()
