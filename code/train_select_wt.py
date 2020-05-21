# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:01:02 2020

@author: 23826
"""

import pandas as pd

feature_test = pd.read_csv('../feature/train/allfeature_train.csv')

#这里将正常样本和故障征兆样本合并

#feature_final = pd.concat([feature_normal,feature_fault])

#重置索引，否则可能造成索引混乱

#feature_final = feature_final.reset_index(drop=True)

#可以修改以下list调整需要留下的特征

feature_selected_list = ['DE_cA4','DE_cD4','DE_cD3','DE_cD2','DE_cD1',
                         'FE_cA4','FE_cD4','FE_cD3','FE_cD2','FE_cD1',
                         'RPM','label']

feature_selected = feature_test[feature_selected_list]
#筛选后特征保存

feature_selected.to_csv('../feature/train/train_selected_wt.csv',index=False)
