import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
class DataSpread:
    def __init__(self,file_path):
        self.file_path = file_path
    def handle(self):
        data = pd.read_csv(self.file_path, header=0)
        data_group = data.groupby(by='finish_time')
        order_statics = {'date': [], 'count': []}
        for i, j in data_group:
            order_statics['date'].append(i)
            order_statics['count'].append(len(j))
        order_statics_pd = pd.DataFrame.from_dict(order_statics)
        order_count_max = order_statics_pd.describe()['count']['max']
        order_count_min = order_statics_pd.describe()['count']['min']
        range = order_count_max - order_count_min
        group_num = 7  # 一共分七组
        dif_value = range / group_num  # 每组的长度
        x_data = np.arange(order_count_min, order_count_max + 2 * dif_value, dif_value, int)
        # 构成新的分布数组，key 是最小到最大订单数量，value是落在区间内的天数
        spread_data = {}
        for little_index in np.arange(0, x_data.size, 1):
            for row_index in order_statics_pd.index:
                if (order_statics_pd.loc[row_index][0] >= x_data[little_index]) and (
                        order_statics_pd.loc[row_index][0] < x_data[little_index + 1]):
                    if str(x_data[little_index]) not in spread_data.keys():
                        spread_data[str(x_data[little_index])] = 1
                    else:
                        spread_data[str(x_data[little_index])] = spread_data[str(x_data[little_index])] + 1

        result_spread_data = {'limit_orders': [], 'day_count': []}
        for order_item in spread_data.keys():
            result_spread_data['limit_orders'].append(int(order_item))
            result_spread_data['day_count'].append(spread_data[order_item])
        width=30
        #可以显示中文添加设置
        plt.rcParams['font.family'] = ['sans-serif']
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.bar(x=result_spread_data['limit_orders'], height=result_spread_data['day_count'],width=width)
        #设置x坐标值
        plt.xticks(result_spread_data['limit_orders'], result_spread_data['limit_orders'])
        plt.title('订单分布')
        #设置数字标签
        for a, b in zip(result_spread_data['limit_orders'], result_spread_data['day_count']):
            plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=7)
        plt.show()
        return result_spread_data
    def save_to_csv(self):
        data_dict = self.handle()
        spread_pd = pd.DataFrame.from_dict(data_dict)
        spread_pd.to_csv('./dlj_dlj_order_after_spread.csv')

model = DataSpread('./dlj_dlj_order_after_preprocresult.csv')
model.save_to_csv()