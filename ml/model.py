import numpy as np


def train_test_split(x, y, test_ratio=0.25, seed=None):
    if seed:
        np.random.seed(seed)

    permutation = np.random.permutation(len(x))  # 生成一个从0到149的乱序列表
    test_size = int(len(x) * test_ratio)  # 测试数据集的个数
    x_test = np.array([x[i] for i in permutation[:test_size]])
    y_test = np.array([y[i] for i in permutation[:test_size]])
    x_train = np.array([x[i] for i in permutation[test_size:]])
    y_train = np.array([y[i] for i in permutation[test_size:]])
    return [x_train, x_test, y_train, y_test]
