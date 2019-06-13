'''
    数据离散化处理
'''
import pandas as pd
import math
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
class DataFormat:
    '''
        制定要处理的文件
    '''
    def __init__(self,file_path):
        self.file_path = file_path
        self.k = 4

    def erase_empty_row(self):
        data = pd.read_csv(self.file_path, header=0)
        # 删除order_amount小于等于1的行
        data = data[data['order_amount'] > 1]
        # 删除所有存在属性为空的行
        data.dropna(axis=0, how='any', inplace=True)
        return data

    '''
        添加属性，     
    '''
    def add_hour_attribute(self):
        data = self.erase_empty_row()
        #添加列进行配置
        data['use_hour'] = data['use_count'].apply(lambda x: math.ceil(x/(60*30))*0.5)
        #该行和上一行代码功能相同
        data['use_hour'] = data.apply(lambda x: math.ceil(x['use_count']/(60*30))*0.5, axis=1)
        return data


    '''
        数据切片，
    '''
    def same_width_lisan(self,data):
        # 每四个进行切片
        k = self.k
        labels = range(k)
        # pd.cut 进行切片,每个间距的元素个数是k个
        return pd.cut(data, k, labels=labels)

    '''
        根据频率进行切片
    '''
    def same_freq_lisan(self, data):
        k = self.k
        w = [1.0 * i / k for i in range(k + 1)]
        #前4个元素分别是count  mean  std min，所以越过这四个
        w = data.describe(percentiles=w)[4:4 + k + 1]
        # 得到0 0。25  0.5  0.75的分位数，则进行cut的时候，制定w中的元素作为边界
        w[0] = w[0] * (1 - 1e-10)
        d2 = pd.cut(data, w, labels=range(k))
        return d2

    '''
         KMeans??
    '''

    def k_means_lisan(self, data):
        k = self.k
        kmodel = KMeans(n_clusters=k, n_jobs=1)  # ???? n_jobs并行度
        kmodel.fit(data.values.reshape((len(data), 1)))  # ????
        c = pd.DataFrame(kmodel.cluster_centers_).sort_values(0,ascending=True)  # ???????????????????
        w = pd.rolling_mean(c, 2).iloc[1:]  # ????????????
        w = [0] + list(w[0]) + [data.max()]  # ???????
        d3 = pd.cut(data, w, labels=range(k))
        return d3

    '''
        ????
    '''
    def cluster_plot(self,d,k):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        plt.figure(figsize =(8,3))
        for j in range(0,k):
            plt.plot(data[d==j], [j for i in d[d==j]],'o')
        plt.ylim(-0.5,k-0.5)
        return plt

'''
    ????????????(???use_count?)
'''

model = DataFormat('./dlj_dlj_order.csv')
data = model.add_hour_attribute()
data = data['use_hour'].copy()
#d1 = model.same_width_lisan(data)
#model.cluster_plot(d1,model.k).show()
d2 = model.same_freq_lisan(data)
#model.cluster_plot(d2,model.k).show()

#d3 = model.k_means_lisan(data)
#model.cluster_plot(d3,model.k).show()
