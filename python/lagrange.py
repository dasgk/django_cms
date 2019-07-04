'''
    拉格朗日插值算法
'''
import pandas as pd
from pandas import DataFrame
from scipy.interpolate import lagrange

class LagrangeInsert():
    def __init__(self):
        self.x =[1,3,4,6,7,9,0,10,11,20,23,26]


    # s是列向量 n是被插值的位置， k是取前后k个数，默认是5
    def ployinterp(self,s,n,k=5):
        y=s[list(range(n-k,n)) +list(range(n+1, n+1+k))]
        y=y[y.notnull()]
        return lagrange(y.index, list(y))(n)

    def handle(self):
        data = {'x':self.x}
        data = DataFrame.from_dict(data)
        for i in data.columns:
            for j in range(len(data)):
                if data[i][j] == 0:
                    data[i][j] = self.ployinterp(data[i],j)
                    print(i,j,data[i][j])

lagrange_modal = LagrangeInsert()
lagrange_modal.handle()
