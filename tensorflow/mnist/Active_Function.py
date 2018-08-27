import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# 创建输入数据
x_data = np.linspace(-7, 7, 180)  # -7到7等间隔的180个点


# 激活函数的原始实现
def sigmoid(inputs):
    return [1 / float(1 + np.exp(-x)) for x in inputs]


def relu(inputs):
    return [x * (x > 0) for x in inputs]


def tanh(inputs):
    return [(np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x)) for x in inputs]


def softplus(inputs):
    return [np.log(1 + np.exp(x)) for x in inputs]


# 有关激活函数,可以参考维基百科https://zh.wikipedia.org/wiki/激活函数

# 经过TensorFlow的激活函数处理的各个Y值
y_sigmoid = tf.nn.sigmoid(x_data)
y_relu = tf.nn.relu(x_data)
y_tanh = tf.nn.tanh(x_data)
y_softplus = tf.nn.softplus(x_data)

# 创建会话
sess = tf.Session()
y_sigmoid, y_relu, y_tanh, y_softplus = sess.run([y_sigmoid, y_relu, y_tanh, y_softplus])
print(y_sigmoid, y_relu, y_tanh, y_softplus)

# 创建各个激活函数的图像
plt.subplot(221)  # 2行2列的第1个位置
plt.plot(x_data, y_sigmoid, 'r', label='Sigmoid')
plt.ylim(-0.2, 1.2)
plt.legend(loc='best')  # 标签自动显示在最合适的位置

plt.subplot(222)
plt.plot(x_data, y_relu, 'r', label='Relu')
plt.ylim(-1, 6)
plt.legend(loc='best')

plt.subplot(223)
plt.plot(x_data, y_tanh, 'r', label='Tanh')
plt.ylim(-1.3, 1.3)
plt.legend(loc='best')

plt.subplot(224)
plt.plot(x_data, y_softplus, 'r', label='SoftPlus')
plt.ylim(-1, 6)
plt.legend(loc='best')

plt.show()

# 关闭会话
sess.close()
