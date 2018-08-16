from sklearn import datasets
import matplotlib.pyplot as plt
from ml.model import train_test_split
from ml.knn import KNeighborsClassifier

iris = datasets.load_digits()
x = iris.data
y = iris.target
print(x.shape)
print(iris.DESCR)
x_train, x_test, y_train, y_test = train_test_split(x, y, seed=666)
# X中第1个元素的图像x
plt.imshow(x[0].reshape(8, 8))  # 打印图片
plt.show()
print('图片上的值为:', y[1])

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
predict = knn.predict(x_test)  # 预测的结果
print('预测结果为:', predict)
print('实际结果为:', y_test)
print('预测准确率为:', sum(predict == y_test) / len(y_test) * 100, '%')
