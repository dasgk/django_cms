import pandas as pd
'''
    进行数据探索，检测异常值
'''
data_sample_path = './dlj_dlj_order.csv'
data = pd.read_csv(data_sample_path)
#删除order_amount为0的缺失值
data = data[data['order_amount']>1]
#分析异常值，也就是use_count,使用3倍标准差原则，也就是测定值和平均值的偏差超过3倍标准差的话，则视为异常值
data_std = data.describe()['use_count']['std']
data_mean = data.describe()['use_count']['mean']

for indexs in data.index:
    print(indexs)
    print(data.loc[indexs].values[0:-1])
    exit()
#再次过滤异常值，使用最大最小值进行异常值顾虑最小是5，最大是8*60*60
data_min = 5
data_max = 8*60*60
