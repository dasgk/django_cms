'''
    ?????????????
'''
import pandas as pd
import math
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
class DataFormat:
    '''
        ???????????????
    '''
    def __init__(self,file_path):
        self.file_path = file_path
        self.k = 4

    def erase_empty_row(self):
        data = pd.read_csv(self.file_path, header=0)
        # ??order_amount?0????
        data = data[data['order_amount'] > 1]
        # ???????
        data.dropna(axis=0, how='any', inplace=True)
        return data

    '''
        ?????????????????        
    '''
    def add_hour_attribute(self):
        data = self.erase_empty_row()
        #????????????Series??apply????
        data['use_hour'] = data['use_count'].apply(lambda x: math.ceil(x/(60*30))*0.5)
        #????????,??dataframe?apply???????axis=1
        data['use_hour'] = data.apply(lambda x: math.ceil(x['use_count']/(60*30))*0.5, axis=1)
        return data


    '''
        ????
    '''
    def same_width_lisan(self,data):
        # ?????
        k = self.k
        labels = range(k)
        # pd.cut ?????????x??????,?????????int??????????k?????
        return pd.cut(data, k, labels=labels)

    '''
        ????
    '''
    def same_freq_lisan(self, data):
        k = self.k
        w = [1.0 * i / k for i in range(k + 1)]
        w = data.describe(percentiles=w)[4:4 + k + 1]
        w[0] = w[0] * (1 - 1e-10)
        # cut???????w??????????????????
        d2 = pd.cut(data, w, labels=range(k))
        return d2

    '''
         KMeans??
    '''

    def k_means_lisan(self, data):
        k = self.k
        kmodel = KMeans(n_clusters=k, n_jobs=1)  # ???? n_jobs????????CPU??
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
model.cluster_plot(d2,model.k).show()

#d3 = model.k_means_lisan(data)
#model.cluster_plot(d3,model.k).show()
