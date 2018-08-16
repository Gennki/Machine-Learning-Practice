from math import sqrt
import numpy as np
from collections import Counter


class KNeighborsClassifier(object):
    def __init__(self, k=5):
        self.k = k

    def fit(self, x_train, y_train):
        assert 1 <= self.k <= x_train.shape[0], 'k的范围不符合要求'
        assert x_train.shape[0] == y_train.shape[0], '请检查x_train的样本数和y_train的数量是否一致'
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_predict):
        assert x_predict.ndim >= 2, '需要至少2维的矩阵'
        assert x_predict.shape[1] == self.x_train.shape[1], '目标向量的特征数量需要和x_train的特征数量相同'
        y_predict = []
        for i in range(len(x_predict)):
            distances = [sqrt(np.sum((j - x_predict[i]) ** 2)) for j in self.x_train]
            index = np.argsort(distances)   # 距离有小到大排序后的索引,例如distances中原来最小的距离为0.1,排在第3位,那么index[0]就是3
            nearest = [self.y_train[i] for i in index[:self.k]]  # a到距离最近的k个点的肿瘤情况
            counter = Counter(nearest)  # 统计k个点中,恶性肿瘤和两情肿瘤出现的次数,例如Counter({1: 2, 0: 1})代表良性肿瘤2次,恶性肿瘤1次
            y_predict.append(counter.most_common(1)[0][0])  # counter.most_common(1)表示从counter中取出出现次数最多的,这里则为[(1, 2)],之后取[0][0]则为1,表示良性肿瘤
        return np.array(y_predict)
