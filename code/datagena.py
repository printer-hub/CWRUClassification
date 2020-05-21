# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:03:10 2020

@author: 23826
"""
import pandas as pd
import os

def datagena(path_machine,out_machine):
    #该路径下所有文件名列表
    dirs_machine = os.listdir(path_machine) 
    dirs_machine.sort()
    #该路径下所有问件路径列表
    rpath_machine = [os.path.join(path_machine,name) for name in dirs_machine] #建立path_machine下所有文件的path列表
    #建立输入数据的dataframe对象
    df_out = pd.DataFrame()
    for i in range(len(rpath_machine)):
        df_machine=pd.read_csv(rpath_machine[i])
    #打标签
        if ('B' in dirs_machine[i]):
            df_machine['label']=1
        if('OR' in dirs_machine[i]):
            df_machine['label']=2
        if('IR' in dirs_machine[i]):
            df_machine['label']=3
        if('NORMAL' in dirs_machine[i]):
            df_machine['label']=0
    #拼接
        df_out=pd.concat([df_out,df_machine],ignore_index=True,axis=0,sort=False)
    #按标签排序
        df_out=df_out.sort_values('label')
    df_out.to_csv(out_machine,index=False)
    return df_out
data_gena=datagena("../datatw/train","../datagena/datagena.csv")
    