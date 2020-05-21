import pandas as pd

feature_test = pd.read_csv('../feature/test/allfeature_test.csv')


feature_selected_list = ['DE_time_std','DE_time_ptp',
                         'DE_time_skew','DE_time_wavefactor','DE_time_peakfactor','DE_time_pulse',
                         'DE_max1_point','DE_max2_point','DE_max3_point','DE_max1_ratio','DE_max2_ratio','DE_max3_ratio',
                         'DE_cA4','DE_cD4','DE_cD3','DE_cD2','DE_cD1',
                         'FE_time_std','FE_time_ptp',
                         'FE_time_skew','FE_time_wavefactor','FE_time_peakfactor','FE_time_pulse',
                         'FE_max1_point','FE_max2_point','FE_max3_point','FE_max1_ratio','FE_max2_ratio','FE_max3_ratio',
                         'FE_cA4','FE_cD4','FE_cD3','FE_cD2','FE_cD1',
                         'RPM','filename']

feature_selected = feature_test[feature_selected_list]
#筛选后特征保存

feature_selected.to_csv('../feature/test/test_selected_all.csv',index=False)



