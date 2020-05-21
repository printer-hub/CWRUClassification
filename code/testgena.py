# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 20:22:44 2020

@author: 23826
"""
import pandas as pd
import os

def testgena(path_machine,out_machine):
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
        df_machine['filename']=dirs_machine[i][0:-6]
    #拼接
        df_out=pd.concat([df_out,df_machine],ignore_index=True,axis=0,sort=False)
    #按标签排序
        df_out=df_out.sort_values('filename')
    df_out.to_csv(out_machine,index=False)
    return df_out
test_gena=testgena("../datatw/test","../datagena/testgena.csv")
    
