import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class DataPreproc:
    def __init__(self,file_path):
        self.file_path = file_path
    def erase_empty_row(self):
        #data_sample_path = './dlj_dlj_order.csv'
        data = pd.read_csv(self.file_path, header=0)
        # 删除order_amount为0的缺失值
        data = data[data['order_amount'] > 1]
        # 删除有空值的行
        data.dropna(axis=0, how='any', inplace=True)
        return data
    def erase_unexpect_row(self,data):
        # 分析异常值，也就是use_count,使用3倍标准差原则，也就是测定值和平均值的偏差超过3倍标准差的话，则视为异常值
        data_std = data.describe()['use_count']['std']
        data_std_3 = data_std * 3
        data_mean = data.describe()['use_count']['mean']
        data_min = 10  # 最短10秒钟
        data_max = 60 * 60 * 6  # 最长8小时
        except_count = 0
        for row_index in data.index:
            # 输出第row_index行的第4列的数据
            current_use_count = data.loc[row_index][4]
            # 判断当前值是否是异常值，如果当前值和平均值的差值是否在3个标准差之内
            value_dif = 0
            if current_use_count > data_mean:
                value_dif = current_use_count - data_mean
            else:
                value_dif = data_mean - value_dif
            if value_dif > data_std_3:
                data.drop(index=row_index, inplace=True)
                print(str(row_index) + '行数据，与平均值差距超过3倍标准差-已删除')
                except_count += 1
                continue
            if current_use_count <= data_min:
                data.drop(index=row_index, inplace=True)
                print(str(row_index) + '行数据，小于最小值-已删除')
                except_count += 1
                continue
            if current_use_count >= data_max:
                data.drop(index=row_index, inplace=True)
                print(str(row_index) + '行数据，大于最大值-已删除')
                except_count += 1
                continue
        # 进行数据处理，将finish_time修改为day为单位
        data['finish_time'] = data['finish_time'].map(lambda x: x[0:10])
        return data
    def get_target_data(self,data):
        # 进行数据分离，去掉所有rent_museum_id不是5的数据集,只看牛首山博物馆的
        data = data[data['rent_museum_id'] == 5]
        # 只看已完成的订单
        data = data[data['order_status'] == 5]
        return data
    def save_to_data(self):
        data = self.erase_empty_row()
        data = self.erase_unexpect_row(data)
        data = self.get_target_data(data)
        data.to_csv('./dlj_dlj_order_after_preprocresult.csv')

model = DataPreproc('./dlj_dlj_order.csv')
model.save_to_data()

