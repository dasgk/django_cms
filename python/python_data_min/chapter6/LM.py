#-*- coding:UTF-8 -*-
import pandas as pd
from random import shuffle #引入随机打乱函数
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib
from keras.models import Sequential
from keras.layers.core import Dense,Activation

inputfile='./data/model.xls'
netfile = './data/net.model'
data = pd.read_excel(inputfile)
data = data.as_matrix() #将表格转为矩阵
shuffle(data) # 打乱函数

p=0.8 #80%的数据作为训练数据  20的为测试数据
train = data[:int(len(data)*p),:]  #p是浮点数，需要强制转换为int
test = data[int(len(data)*p):,:]

net = Sequential()
net.add(Dense(3,10)) #添加输入层3个节点到隐藏层10个节点的连接
net.add(Activation('relu')) # 隐藏层使用激活函数relu
net.add(Dense(10,1)) #隐藏层10个节点到输出层1个节点的连接
net.add(Activation('sigmoid')) #使用激活函数 sigmoid
net.compile(loss="binary_crossentropy",optimizer='adam',class_mode='binary') #编译模型使用adam求解
net.fit(train[:,:3],train[:,3:],nb_epoch=1000,batch_size=1) #训练模型，使用1000次
net.save_weights(netfile)

predict_result = net.predict_classes(test[:,:3]).reshape(len(test)) #将预测结果进行变形处理
'''
    这里需要注意的是keras使用predict给出预测率，predict_classes才是预测类别，两者的结果都是n*1的维数组
'''
