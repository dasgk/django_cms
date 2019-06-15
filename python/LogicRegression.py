'''
    逻辑回归代码案例
'''
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR
import pandas as pd
class LogicRegression:
    def __init__(self, path):
        self.file_path = path
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path,header=0,encoding="gbk")

    def data_proc(self):
        self.load_data()
        # iloc，完全基于位置的索引,[]中的第一个值是从第几行到第几行，第二个是从第几列到第几列
        x = self.data.iloc[:,:8].as_matrix()
        y = self.data.iloc[:,8].as_matrix()
        #先使用随机变量模型进行属性的筛选
        rlr = RLR()
        rlr.fit(x,y)#训练模型
        rlr.get_support()#获取特征筛选结果，也可以通过.scores获得各个特征的分数

        print("有效特征为%s" % ','.join(self.data.columns[rlr.get_support()]))
        x = self.data[data.columns[rlr.get_support()]].as_matrix()#筛选之后的特征
        rlr.get_support()
        lr = LR(class_weight={0:0.9, 1:0.1}) # 分类权重，避免误分类代价比较高时使用，class_weight='balanced'自行处理，或者像代码中那样设置
        #lr.fit(x, y,sample_weight=[1,2,3,5,4,9,8,10])
        lr.fit(x, y, sample_weight=[1, 2, 3, 5, 4]) #样本权重，设置每一行数据的重要性，一行数据一个值
        result = lr.predict([[24,2,2,0,28,17.3,1.79,3.06]])
        print('模型的正确率是：%s,预测结果是 %d'% (lr.score(x,y) , result))

model = LogicRegression('./bankloan.csv')
model.data_proc()




