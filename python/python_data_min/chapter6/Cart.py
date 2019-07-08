#-*- coding:UTF-8 -*-
import pandas as pd
from random import shuffle #引入随机打乱函数
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

inputfile='./data/model.xls'
data = pd.read_excel(inputfile)
data = data.as_matrix() #将表格转为矩阵
shuffle(data) # 打乱函数

p=0.8 #80%的数据作为训练数据  20的为测试数据
train = data[:int(len(data)*p),:]  #p是浮点数，需要强制转换为int
test = data[int(len(data)*p):,:]
tree = DecisionTreeClassifier()
tree.fit(train[:,:3], train[:,3])

treefile = './data/treefile'
joblib.dump(tree,treefile)

print(tree.predict(test[:,:3]))





