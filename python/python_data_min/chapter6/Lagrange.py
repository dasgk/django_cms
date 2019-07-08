#-*- coding: utf-8 -*-
import pandas as pd
from scipy.interpolate import lagrange #拉格朗日函数

inputfile = './data/missing_data.xls'
outputfile = './data/missing_lagrange_processed.xls'

data = pd.read_excel(inputfile, header=None)


# 自定义列向量插值函数
# s为列向量，n为被插值的位置，k是前后取k个数据个数，默认是5
def ployinterp_columns(s, n, k=5):
    #s是传递进来的Series
    y = s[list(range(n - k, n)) + list(range(n + 1, n + 1 + k))]
    #经过转换y是Series
    y = y[y.notnull()]  # 剔除空值
    #y.index是 pandas.core.indexes.numeric.Int64Index
    return lagrange(y.index, list(y))(n)  # 返回插值的结果


for i in data.columns:
    for j in range(len(data)):
        # pandas是按照先列索引，然后行索引进行数据查找和配置的
        if (data[i].isnull())[j]:  # 如果为空则进行插值
            data[i][j] = ployinterp_columns(data[i], j)
data.to_excel(outputfile, header=None, index=False) #输出结果