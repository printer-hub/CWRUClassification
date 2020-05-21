# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:22:06 2020

@author: 23826
"""
#对每个设备只输出一个预测值
#对属于同一设备文件的预测结果进行整合，选择出现次数最多的结果作为该设备最后的预测结果

import pandas as pd
tw_result=pd.read_csv('../result/result4.csv')
unify_result=tw_result.groupby('filename').agg(lambda x: x.value_counts().index[0]).reset_index()
columns=['label','filename']
unify_result.to_csv('../result/result.csv',index=False,columns=columns)
