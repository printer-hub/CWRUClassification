# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:51:06 2020

@author: 23826
"""

import pandas as pd
import numpy as np
import os
from scipy import stats
from scipy import signal
import pywt
from pywt import wavedec
#列名定义
df_out_columns = ['time_mean','time_std','time_max','time_min','time_rms',
                  'time_ptp','time_median','time_iqr','time_pr',
                  'time_skew','time_kurtosis','time_var','time_amp',
                  'time_smr','time_wavefactor','time_peakfactor',
                  'time_pulse','time_margin',
                  'max1_point','max2_point','max3_point',
                  'max1_ratio','max2_ratio','max3_ratio',
                  'max1_value','max2_value','max3_value','cA4','cD4','cD3','cD2','cD1']

DE_columns = ['DE_'+ i for i in df_out_columns]
FE_columns = ['FE_'+ i for i in df_out_columns]
RPM_columns = ['RPM']
label_columns = ['label']
#label_columns = ['label']
full_columns = DE_columns + FE_columns + RPM_columns + label_columns
#full_columns = DE_columns + FE_columns + label_columns

def featureget(df_line):
    #提取时域特征
    time_mean = df_line.mean()#均值
    time_std = df_line.std()#标准差
    time_max = df_line.max()
    time_min = df_line.min()
    time_rms = np.sqrt(np.square(df_line).mean().astype(np.float64))#均方根
    time_ptp = np.asarray(df_line).ptp()#峰峰值
    time_median = np.median(df_line)#z中位数
    time_iqr = np.percentile(df_line,75)-np.percentile(df_line,25)#四方位差
    time_pr = np.percentile(df_line,90)-np.percentile(df_line,10)#百分位差
    time_skew = stats.skew(df_line)#偏度
    time_kurtosis = stats.kurtosis(df_line)#峰度
    time_var = np.var(df_line)#方差
    time_amp = np.abs(df_line).mean()#整流平均值
    time_smr = np.square(np.sqrt(np.abs(df_line).astype(np.float64)).mean())#方根幅值
    #下面四个特征需要注意分母为0或接近0问题，可能会发生报错
    time_wavefactor = time_rms/time_amp#波形因子
    time_peakfactor = time_max/time_rms#峰值因子
    time_pulse = time_max/time_amp#脉冲值
    time_margin = time_max/time_smr#裕度
    #提取频域特征倍频能量以及能量占比
    plist_raw = np.fft.fft(list(df_line), n=1024)
    plist = np.abs(plist_raw)
    plist512=plist[0:512]
    plist_energy = (np.square(plist)).sum()
    #前三最大值点与能量占比
    '''
    max1_point=np.argmax(plist512)
    max1_ratio=plist[max1_point]/plist_energy
    plist[max(0,max1_point-5):min(511,max1_point+5)]=0
    max2_point=np.argmax(plist512)
    max2_ratio=plist[max2_point]/plist_energy
    plist[max(0,max2_point-5):min(511,max2_point+5)]=0
    max3_point=np.argmax(plist512)
    max3_ratio=plist[max3_point]/plist_energy
    plist[max(0,max3_point-5):min(511,max3_point+5)]=0
    '''
    #频域特征
    max1_point=np.argmax(plist512)
    max1_ratio=plist[max1_point]/plist_energy    
    max1_value=plist[max1_point]
    plist[max1_point]=0
    max2_point=np.argmax(plist512)
    max2_ratio=plist[max2_point]/plist_energy
    max2_value=plist[max2_point]
    plist[max2_point]=0
    max3_point=np.argmax(plist512)
    max3_ratio=plist[max3_point]/plist_energy
    max3_value=plist[max3_point]
    plist[max3_point]=0    
    
    return_list = [time_mean,time_std,time_max,time_min,time_rms,time_ptp, 
    time_median,time_iqr,time_pr,time_skew,time_kurtosis,
    time_var,time_amp,time_smr,time_wavefactor,time_peakfactor,
    time_pulse,time_margin,max1_point,max2_point,max3_point,max1_ratio,max2_ratio,max3_ratio,
    max1_value,max2_value,max3_value]

    return return_list

#时频域特征
params = {}
params['len_piece']=200    
params['wave_layer']=4      
params['wave_win']=38*pow(2,params['wave_layer']-1)-1  

def one_row(arr):
    result_list = []
    arr_add=arr.iloc[:,]
    #print(arr_add)
    for j in range(int(params['wave_win']/params['len_piece'])):
        arr_add =arr_add.append(arr,ignore_index=True)
    cD=wavedec(arr_add,'db10',level=params['wave_layer'])
    #print('cD:'+str(i))
    #print(cD)
    for i in range(params['wave_layer']+1):
        ener_cD = np.square(cD[i]).sum()
        #print(ener_cD)
        list_para = [ener_cD]
        #print('list_para'+list_para)
        result_list.extend(list_para)
        #print(len(result_list))
    #list_label=[label_mean.mean()]
    #result_list.extend(list_label)
    return result_list

df_normal = pd.read_csv('../datagena/datagena.csv')
#df_normal = pd.read_csv('E:/CWRU/new256/datagena.csv')
feature_normal = []
for i in range(0,df_normal.shape[0]):#按行处理
    feature_line = []
    for j in range(0,2):
        a=df_normal.iloc[i,1024*0:1024*(0+1)]
        feature_line.extend(featureget(df_normal.iloc[i,1024*j:1024*(j+1)]))
        feature_line.extend(one_row(df_normal.iloc[i,1024*j:1024*(j+1)]))
    feature_line.append(df_normal['2048'][i])

    #feature_line.append(df_normal['label'][i])
    feature_line.append(df_normal['label'][i])

    feature_normal.append(feature_line)

#输出全特征
feature_normal = pd.DataFrame(feature_normal,columns=full_columns)
feature_normal.to_csv('../feature/train/allfeature_train.csv',index=False)
