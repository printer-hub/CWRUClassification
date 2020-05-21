# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 08:45:32 2020

@author: 23826
"""

import pandas as pd
import numpy as np
import os
import math

#加时间窗
def timewindow(path_machine,out_machine,tw_size=1024,step_size=256):
    #读取机组文件夹下各数据组文件夹的路径并按文件名排序，保证整合时
    #数据组文件夹读取的顺序固定，使接下来的读取以a-e或1-5的顺序进行
    dirs_machine = os.listdir(path_machine) #dirs_machine为对应路径下所有文件的列表
    dirs_machine.sort()
    rpath_machine = [os.path.join(path_machine,name) for name in dirs_machine]#建立path_machine下所有文件的path列表
    #建立输入数据的dataframe对象
    out_name=[]
    for name in dirs_machine:
        name=name[0:-4]+'tw.csv'
        out_name.append(name)
    for i in range(len(rpath_machine)):
        df_out=pd.DataFrame()
        df_machine=pd.read_csv(rpath_machine[i])
        if 'BA_time' in df_machine.columns.values.tolist():
            df_machine=df_machine.drop('BA_time',axis=1)
        sample_num=df_machine.shape[0]  #行数
        tw_num=math.floor((sample_num-tw_size)/step_size)  #整合后的时间窗数
        #np_machine=np.array()
        for k in range(tw_num):
            np_temp=np.array(df_machine.ix[k*step_size:k*step_size+tw_size-1,:])
            np_tw=np_temp.reshape((1,-1),order='F')
            np_tw=np_tw[0,0:(2*tw_size+1)]
            np_tw=np_tw.reshape((1,-1),order='F')
            df_temp=pd.DataFrame(np_tw)#,index=['0'],columns=range(np.size(np_tw)))
            df_out=pd.concat([df_out,df_temp],axis=0,ignore_index=True)
        opath=[os.path.join(out_machine,name) for name in out_name]
        df_out.to_csv(opath[i],index=False)
    return np_tw

#均衡化
def dataequal(df_tw):
    a=sample_num=df_tw.shape[0]
    index_save=[]
    for k in range(sample_num):
        a=np.random.rand()
        if(a<1/6):
            index_save.append(k)
    df_eq=df_tw.ix[index_save,:]
    return df_eq
temptw=timewindow("../dataset/train","../datatw/train",tw_size=1024,step_size=256)

'''
df_normal1=pd.read_csv('../datatw/train/NORMAL01tw.csv')
df_eq1=dataequal(df_normal1)
df_eq1.to_csv('../datatw/train/NORMAL01tw.csv',index=False)       

df_normal2=pd.read_csv('../datatw/train/NORMAL02tw.csv')
df_eq2=dataequal(df_normal2)
df_eq2.to_csv('../datatw/train/NORMAL02tw.csv',index=False)
'''
