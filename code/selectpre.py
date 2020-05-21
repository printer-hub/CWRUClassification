import numpy as np
import pandas as pd

#对三份预测文件进行比较整合
#对于每一行的预测结果，选择出现次数多的作为最后的预测结果

#例如，三份文件对于第一行数据的预测结果分别为1、1、2，则最后输出1
#如果对于某一行数据，三份文件的预测结果均不一样，则输出result3对这一行的预测结果

arr1 = np.array(pd.read_csv('../result/result1.csv'))
pre1 = arr1[:,0]

arr2 = np.array(pd.read_csv('../result/result2.csv'))
pre2 = arr2[:,0]

arr3 = np.array(pd.read_csv('../result/result3.csv'))
pre3 = arr3[:,0]

pre = []

for i in range(0,pre1.shape[0]):
    if(pre1[i] == pre2[i]):
        pre.append(1)
        pre[i] = pre1[i]
    elif((pre1[i] == pre3[i])or(pre2[i] == pre3[i])):
        pre.append(1)
        pre[i] = pre3[i]
    else:
        pre.append(1)
        pre[i] = pre3[i]

filename = pd.DataFrame(arr1[:,-1],columns = ['filename'])
a = pd.DataFrame(pre,columns = ['label'])
b = pd.concat([a,filename],axis = 1)
b.to_csv('../result/result4.csv',index = False)
