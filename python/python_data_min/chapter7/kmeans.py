#-*- coding:utf-8 -*-

import pandas as pd

inputfile='./data/air_data.csv'
explorefile = './data/data_after_explore.xls'
cleanfile = './data/data_after_clean.xls'


'''
    以下是数据统计
'''
def data_statics():
    data = pd.read_csv(inputfile)
    # percentiles 参数是指定计算多少的分位数表 T是转置方便使用， describe自动计算非空值
    #包括对数据的基本描述   行索引是 count   unique  top  freq
    # 列索引是 每个属性
    explore = data.describe(percentiles=[], include='all')
    # 行索引就是每个属性的名字了， 列索引自然就是  max  min   null
    explore = data.describe(percentiles=[], include='all').T

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



data_clean()




