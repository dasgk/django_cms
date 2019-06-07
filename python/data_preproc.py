import pandas as pd
import numpy as np
'''
    进行数据探索，检测异常值
'''
data_sample_path = './dlj_dlj_order.csv'
data = pd.read_csv(data_sample_path,header=0)
#删除order_amount为0的缺失值
data = data[data['order_amount']>1]
#删除有空值的行
data.dropna(axis=0, how='any', inplace=True)
#分析异常值，也就是use_count,使用3倍标准差原则，也就是测定值和平均值的偏差超过3倍标准差的话，则视为异常值
data_std = data.describe()['use_count']['std']
data_std_3 = data_std*3
data_mean = data.describe()['use_count']['mean']
data_min = 10 #最短10秒钟
data_max = 60*60*6 #最长8小时
(row_count, col_count) = data.shape
except_count = 0
for row_index in data.index:
    # 输出第row_index行的第4列的数据
    current_use_count = data.loc[row_index][4]
    #判断当前值是否是异常值，如果当前值和平均值的差值是否在3个标准差之内
    value_dif = 0
    if current_use_count > data_mean:
        value_dif = current_use_count - data_mean
    else:
        value_dif = data_mean - value_dif
    if value_dif > data_std_3:
        data.drop(index=row_index, inplace=True)
        print(str(row_index) + '行数据，与平均值差距超过3倍标准差-已删除')
        except_count+=1
        continue
    if current_use_count <= data_min:
        data.drop(index=row_index, inplace=True)
        print(str(row_index) + '行数据，小于最小值-已删除')
        except_count+=1
        continue
    if current_use_count >= data_max:
        data.drop(index=row_index, inplace=True)
        print(str(row_index) + '行数据，大于最大值-已删除')
        except_count+=1
        continue
print("处理之前的个数"+str(row_count)+'异常值个数'+str(except_count))
#进行数据处理，将finish_time修改为day为单位
data['finish_time'] = data['finish_time'].map(lambda x: x[0:10])
#进行数据分离，去掉所有rent_museum_id不是5的数据集,只看牛首山博物馆的
data = data[data['rent_museum_id']==5]
#只看已完成的订单
data = data[data['order_status']==5]
# 每天的订单数量进行构建新的dataframe
data_group =data.groupby(by='finish_time')
order_statics = {'date':[],'count':[]}
for i,j in data_group:
    order_statics['date'].append(i)
    order_statics['count'].append(len(j))
order_statics_pd = pd.DataFrame.from_dict(order_statics)
order_count_max = order_statics_pd.describe()['count']['max']
order_count_min = order_statics_pd.describe()['count']['min']
range = order_count_max - order_count_min
group_num = 7 #一共分七组
dif_value = range/group_num
x_data = np.arange(order_count_min,order_count_max,dif_value)
# 将元素类型修改为int
x_data = x_data.astype(int)
# 构成新的分布数组，key 是最小到最大订单数量，value是落在区间内的天数
[rows, cols] = x_data.shape
for i in range(rows):
    for j in range(cols):
        print(x_data[i, j])

spread_pd = {'value_range':[],'day_count':[]}
print(order_statics_pd)
#for row_index in order_statics_pd.index:




