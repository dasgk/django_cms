#-*- coding:utf-8 -*-
from sklearn.metrics import roc_curve #导入roc曲线函数
import pandas as pd
from random import shuffle
from keras.models import Sequential
from keras.layers.core import Dense,Activation
import matplotlib.pyplot as plt  # 导入作图库
'''
    首先进行LM神经网络的机器学习
'''
inputfile = './data/model.xls'
data = pd.read_excel(inputfile)
data = data.as_matrix()
shuffle(data)
p=0.8
train = data[:int(len(data)*p),:]  #前百分之p的数据是训练数据
test = data[int(len(data)*p):,:]   #1-p的数据是测试数据

#建立LM机器学习模型
net = Sequential()
net.add(Dense(input_dim=3,output_dim=10)) #输入节点是3个，隐藏层节点是10个
#所谓激活函数（Activation Function），就是在人工神经网络的神经元上运行的函数，负责将神经元的输入映射到输出端。
net.add(Activation('relu')) #激活函数使用relu ，用于隐藏层神经元输出 f(x) = max(0,x)
net.add(Dense(input_dim =10, output_dim=1)) #隐藏层节点是10个，输出节点是1和
#sigmoid 函数用于将变量映射到0和1之间  f(x)=1/(1+e的x次方)
net.add(Activation('sigmoid')) #激活函数使用sigmod
#优化器使用adam 损失函数使用binary_crossentropy
'''
 损失函数（loss function）或代价函数（cost function）是将随机事件或其有关随机变量的取值映射为非负实数(一般是取预测值和真实值
 的绝对值)以表示该随机事件的“风险”或“损失”的函数。在应用中，损失函数通常作为学习准则与优化问题相联系，即通过最小化损失函数求解和评估模型。
'''
'''
    优化器 optimizer是优化函数，一般是指使用的迭代函数，进行参数的求解，使得损失函数最小
    metrics 衡量指标
        accuracy:分类准确率分数是指所有分类正确的百分比。分类准确率这一衡量分类器的标准比较容易理解，
                 但是它不能告诉你响应值的潜在分布，并且它也不能告诉你分类器犯错的类型。
'''
net.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy']) #编译模型使用adam
#如果说将所有数据训练一次叫做一轮的话。epochs决定了总共进行几轮训练。
#batch_size: 一次训练中, 样本数据被分割成多个小份, 每一小份包含的样本数叫做batch_size
net.fit(train[:,:3], train[:,3:],epochs=1000,batch_size=1)
#preditc_class返回的是类别的索引也就是样本所属类别的标签
predict_result = net.predict_classes(test[:,:3]).reshape(len(test)) #将预测结果进行变形处理
# predict返回的是属于每一个类别的概率，
predict_result = net.predict(test[:,:3]).reshape(len(test))
#roc_curve test[:,3]是真值    predict_result是测试结果属于1的概率估计值
fpr, tpr, thresholds = roc_curve(test[:,3], predict_result, pos_label=1)
plt.plot(fpr, tpr,linewidth=2,label='ROC of LM')
plt.xlabel('False Positive Rate')  #坐标轴标签
plt.ylabel('True Positive Rate') #坐标轴标签
plt.ylim(0,1.05) #边界范围
plt.xlim(0,1.05) #边界范围
plt.legend(loc=4) #图例
plt.show()