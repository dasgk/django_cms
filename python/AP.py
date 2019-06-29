'''
    AP算法实现
'''
from sklearn.cluster import AffinityPropagation
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from itertools import cycle

# generate sample data
class AP():
    def __init__(self):
        # make_blobs generate samples data，param description
        # n_samples the count of sample data
        # n_features the dimension of sample data
        # centers 产生数据的中心点 默认值3
        # clusters 产生数据的中心点，默认值是3
        # cluster_std： 数据集的标准差
        # center_box  中心确定之后的数据边界 默认值(-10,10)
        # shuffle:洗乱数据
        self.centers = [[1, 1], [-1, -1], [1, -1]]
        # 生成实际中心为centers的测试样本300个，X是包含300个(x,y)点的二维数组，labels_true为其对应的真是类别标签
        X, labels_true = make_blobs(n_samples=300, centers=self.centers, cluster_std=0.5,
                                    random_state=0)
        self.X = X
        self.labels_true = labels_true

        #  use ap algorithm to handle
    def handle_ap(self):
        # preference 不指定则为相似度矩阵的中位数
        # damping 阻尼系数，设置在0.5-1之间
        # max_iter 最大迭代次数
        # copy 是否对输入数据进行修改
        # affinity precomputer 或者 euclidean（欧几里得距离）
        # verbose int类型，是否输出详细信息
        # 计算AP
        centers = [[1, 1], [-1, -1], [1, -1]]
        # 生成实际中心为centers的测试样本300个，X是包含300个(x,y)点的二维数组，labels_true为其对应的真是类别标签
        X, labels_true = make_blobs(n_samples=300, centers=centers, cluster_std=0.5,
                                    random_state=0)
        # 计算AP
        ap = AffinityPropagation(preference=-50).fit(X)
        cluster_centers_indices = ap.cluster_centers_indices_  # 预测出的中心点的索引，如[123,23,34]
        labels = ap.labels_  # 预测出的每个数据的类别标签,labels是一个NumPy数组
        n_clusters_ = len(cluster_centers_indices)  # 预测聚类中心的个数
        print('预测的聚类中心个数：%d' % n_clusters_)
        print('同质性：%0.3f' % metrics.homogeneity_score(labels_true, labels))
        print('完整性：%0.3f' % metrics.completeness_score(labels_true, labels))
        print('V-值： % 0.3f' % metrics.v_measure_score(labels_true, labels))
        print('调整后的兰德指数：%0.3f' % metrics.adjusted_rand_score(labels_true, labels))
        print('调整后的互信息： %0.3f' % metrics.adjusted_mutual_info_score(labels_true, labels))
        print('轮廓系数：%0.3f' % metrics.silhouette_score(X, labels, metric='sqeuclidean'))

        # 绘制图表展示
        plt.close('all')  # 关闭所有的图形
        plt.figure(1)  # 产生一个新的图形
        plt.clf()  # 清空当前的图形
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
        # 循环为每个类标记不同的颜色
        for k, col in zip(range(n_clusters_), colors):
            # labels == k 使用k与labels数组中的每个值进行比较
            # 如labels = [1,0],k=0,则‘labels==k’的结果为[False, True]
            class_members = labels == k
            cluster_center = X[cluster_centers_indices[k]]  # 聚类中心的坐标
            plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
            plt.plot(cluster_center[0], cluster_center[1], markerfacecolor=col,
                     markeredgecolor='k', markersize=14)
            for x in X[class_members]:
                plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

        plt.title('预测聚类中心个数：%d' % n_clusters_)
        plt.show()

model = AP()
model.handle_ap()
