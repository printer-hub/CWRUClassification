# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 20:29:00 2020

@author: 23826
"""
import pandas as pd
import numpy as np
import os
import math

def test_timewindow(path_machine,out_machine,tw_size=1024,step_size=256):
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
            np_tw=np_tw[0,0:2*tw_size+1]
            np_tw=np_tw.reshape((1,-1),order='F')
            df_temp=pd.DataFrame(np_tw)#,index=['0'],columns=range(np.size(np_tw)))
            df_out=pd.concat([df_out,df_temp],axis=0,ignore_index=True)
        opath=[os.path.join(out_machine,name) for name in out_name]
        df_out.to_csv(opath[i],index=False)
    return np_temp

tempnp=test_timewindow("../dataset/test","../datatw/test",tw_size=1024,step_size=256)