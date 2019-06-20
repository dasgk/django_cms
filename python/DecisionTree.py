'''
    决策树
'''
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
class DecisionTree:
    def __init__(self,file_path):
        self.file_path = file_path
        self.data = pd.read_csv(self.file_path, encoding='gbk')

    def handle(self):
        data = self.data
        x = data.iloc[:,:8].as_matrix().astype(int)
        y = data.iloc[:,8].as_matrix().astype(int)
        dtc = DTC(criterion='entropy')
        dtc.fit(x,y)
        with open('tree.dot', 'w') as f:
            f = export_graphviz(dtc, feature_names=['年龄','教育','工龄','地址','收入','负债率','信用卡负债','其他负债'], out_file=f)

mode = DecisionTree('./bankloan.csv')
mode.handle()