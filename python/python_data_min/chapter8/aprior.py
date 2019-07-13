import pandas as pd
from sklearn.cluster import KMeans

input_file = "./data/data.xls"
output_file = './data/data_processed.xls'
def data_lisan():

    typelabel = {u'肝气郁结证型系数':'A', u'热毒蕴结证型系数':'B',u'冲任失调证型系数':'C',
             u'气血两虚证型系数':'D',u'脾胃虚弱证型系数':'E',u'肝肾阴虚证型系数':"F"}
    k=4 #需要进行的聚类类别
    result = pd.DataFrame()
    #读取数据并进行聚类分析
    data = pd.read_excel(input_file)
    keys = list(typelabel.keys())
    for i in range(len(keys)):
        print(u'正在进行%s的聚类:' % keys[i])
        kmodel = KMeans(n_clusters=k)
        kmodel.fit(data[keys[i]].as_matrix().reshape(-1,1))
        # 聚类中心
        r1 = pd.DataFrame(kmodel.cluster_centers_, columns=[typelabel[keys[i]]])
        r2 = pd.Series(kmodel.labels_).value_counts() # 分类统计
        r2 = pd.DataFrame(r2, columns=[typelabel[keys[i]]+'n'])
        r = pd.concat([r1, r2], axis=1) #匹配聚类中心和类别数目
        r.index = [1,2,3,4]
        r[typelabel[keys[i]]].rolling(2).mean() #用来计算2列的均值，以此为边界点
        r[typelabel[keys[i]]][1] = 0.0
        result = result.append(r.T)
    result.to_excel(output_file)
data_lisan()