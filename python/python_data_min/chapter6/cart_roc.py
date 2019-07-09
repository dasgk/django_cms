# -*- coding:utf-8 -*-
from random import shuffle
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

inputfile = './data/model.xls'
data = pd.read_excel(inputfile)
data = data.as_matrix()
shuffle(data)  #将数据打乱
p = 0.8
train = data[:int(len(data) * p), :]
test = data[int(len(data) * p):, :]
dt = DecisionTreeClassifier()
dt.fit(train[:,:3], train[:,3])
predict_result = dt.predict(test[:,:3]) # 返回测试数据的预测值
from sklearn.metrics import roc_curve #导入roc曲线函数
#predict_proba 返回的是每个测试数据为每种结果的概率值估计
#fpr 是假阳性概率    tpr是真阳性概率， roc曲线约靠近左上角，越好, pos_label 指的是阳性的标签值是1
#test[:,3] 是真值   dt.predict_proba(test[:,:3])[:1] 指的是每个测试值的阳性概率估计值
fpr, tpr, thresholds = roc_curve(test[:,3], dt.predict_proba(test[:,:3])[:,1], pos_label=1)
import matplotlib.pyplot as plt
plt.plot(fpr,tpr,linewidth=2,label='roc of cart')
plt.xlabel('False Positive Rate') #坐标轴标签
plt.ylabel('True Positive Rate') #坐标轴标签
plt.ylim(0,1.05) #边界范围
plt.xlim(0,1.05) #边界范围
plt.legend(loc=4) #图例
plt.show()