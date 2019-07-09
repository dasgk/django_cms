#-*- coding:utf-8 -*-
'''
    混淆矩阵，也称误差矩阵，是表示精度的一种常用方式用n*n的矩阵来表示
    在人工智能中，混淆矩阵（confusion matrix）是可视化工具，特别用于
    监督学习，在无监督学习一般叫做匹配矩阵。在图像精度评价中，主要用
    于比较分类结果和实际测得值，可以把分类结果的精度显示在一个混淆矩阵里面
    混淆矩阵的每一列代表了预测类别 [2]  ，每一列的总数表示预测为该类别的数据
    的数目；每一行代表了数据的真实归属类别 [2]  ，每一行的数据总数表示该类别
    的数据实例的数目。每一列中的数值表示真实数据被预测为该类的数目：如下图，
    第一行第一列中的43表示有43个实际归属第一类的实例被预测为第一类，同理，
    第一行第二列的2表示有2个实际归属为第一类的实例被错误预测为第二类。
'''

def cm_plot(y, yp):
    from sklearn.metrics import confusion_matrix  # 导入混淆矩阵函数

    cm = confusion_matrix(y, yp)  # 混淆矩阵 y是真值  yp是预测的值

    import matplotlib.pyplot as plt  # 导入作图库
    plt.matshow(cm, cmap=plt.cm.Greens)  # 画混淆矩阵图，配色风格使用cm.Greens，更多风格请参考官网。
    plt.colorbar()  # 颜色标签

    for x in range(len(cm)):  # 数据标签
        for y in range(len(cm)):
            #annotate()方法提供辅助函数，使标注变得容易。 在标注中，有两个要考虑的点：由参数xy表示的标注位置和xytext的文本位置。 这两个参数都是(x, y)元组。
            # cm[x, y] 是标注的内容
            plt.annotate(cm[x, y], xy=(x, y), horizontalalignment='center', verticalalignment='center')

    plt.ylabel('True label')  # 坐标轴标签
    plt.xlabel('Predicted label')  # 坐标轴标签
    return plt