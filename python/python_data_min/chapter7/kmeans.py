#-*- coding:utf-8 -*-

import pandas as pd
# sklearn.cluster 是聚类子库
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

inputfile='./data/air_data.csv'
explorefile = './data/data_after_explore.xls'
cleanfile = './data/data_after_clean.xls'

input_score = './data/zscoredata.xls'
output_score = './data/out_zscoreddata.xls'

'''
    以下是数据统计
'''
def data_statics():
    data = pd.read_csv(inputfile)
    # percentiles 参数是指定计算多少的分位数表 T是转置方便使用， describe自动计算非空值
    #包括对数据的基本描述   行索引是 count   unique  top  freq
    # 列索引是 每个属性
    # percentiles,这个参数可以设定数值型特征的统计量，默认是[.25, .5, .75],
    # 也就是返回25%，50%，75%数据量时的数字，但是这个可以修改的，如果是空的则返回50%的分位数
    # 行索引就是每个属性的名字了， 列索引自然就是  max  min   null
    # include，这个参数默认是只计算数值型特征的统计量，当输入include=['O']，会计算离散型变量的统计特征，all则计算所有
    #  unique   top  freq
    #  count:非空值总数   mean:非空值的平均值   unique: 唯一值数   top: 频数最高者  freq: 最高频数
    explore = data.describe(percentiles=[]).T
    # count是非空值的数量。手动计算空值的数量,对每列进行操作
    explore['null'] = len(data) - explore['count']
    explore = explore[['null','max','min']]
    explore.columns =[u'空值数',u'最大值',u'最小值'] #表头重命名
    explore.to_excel(explorefile)

def data_clean():
    data = pd.read_csv(inputfile)
    #保留票价非零  或者平均折扣与总飞行公里数同时为0的数据
    data=data[data['SUM_YR_1'].notnull() & data['SUM_YR_2'].notnull()]
    # 删除票价为空的行记录
    index1 = data['SUM_YR_1'].notnull()
    index2 = data['SUM_YR_2'].notnull()
    index3 = (data['SEG_KM_SUM']==0) & (data['avg_discount'] == 0)#规则是与
    data = data[index1 | index2 | index3] #这里规则是或
    data.to_excel(cleanfile)


def data_score():
    data = pd.read_excel(input_score)
    #标准化变换
    data = (data-data.mean(axis=0))/(data-data.std(axis=0))
    data.columns = ['Z' + i for i in data.columns]
    data.to_excel(output_score)


def kmeans():
    #header 指定列名行 默认值是0，取第一行是作为列名,不含列名 则 header=None
    # names 可以指定列的名字
    data = pd.read_excel(output_score, header=0,init='random')
    k = 5
    kmodel = KMeans(n_clusters=k)
    # 进行训练
    kmodel.fit(data)
    # 进行预测
    kmodel.predict(data)
    # 训练之后直接预测
    y_= kmodel.fit_predict(data)
    # 返回的是np.ndarray
    labels = kmodel.labels_# 每行的标签，
    # 是 k个类的值
    print("输出类别的标签" ,np.unique(labels))
    # 输出每个类别
    for i in range(len(np.unique(labels))):
        print('类别:',i,'数量：',len(data[y_==i]))
    #聚类中心
    # 不使用科学计数法
    np.set_printoptions(suppress=True)
    np.set_printoptions(precision=4)
    print(kmodel.cluster_centers_)


kmeans()
