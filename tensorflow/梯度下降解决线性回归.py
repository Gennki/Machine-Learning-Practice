import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 创建数据
x_data = np.random.random(100)
y_data = 3 * x_data + np.random.normal(0, 0.1, size=100)

# 创建图像1,显示100个随机的点
plt.plot(x_data, y_data, 'rx', label='Original Data')
plt.legend()  # 可以让label绘制出来
plt.show()

# 构建线性回归模型
W = tf.Variable(tf.random_uniform([1], -1, 1))  # 初始化权重
b = tf.Variable(tf.zeros([1]))  # 初始化偏移量
y = W * x_data + b

# 定义损失函数
loss = tf.reduce_mean(tf.square(y - y_data))

# 用梯度下降优化器来优化我们的损失函数
optimizer = tf.train.GradientDescentOptimizer(0.5)  # 参数为学习率
train = optimizer.minimize(loss)

# 初始化数据流图中的所有变量
init = tf.global_variables_initializer()

# 使用会话
with tf.Session() as sess:
    sess.run(init)
    for i in range(2000):
        sess.run(train)
        print("loss=%s,Weight=%s,Bias=%s" % (sess.run(loss), sess.run(W), sess.run(b)))

    # 绘制拟合后的图像
    plt.plot(x_data, y_data, 'rx', label='Original Data')
    plt.legend()  # 可以让label绘制出来
    plt.plot(x_data, sess.run(W) * x_data + sess.run(b), label='Fitted Line')
    plt.legend()
    plt.show()
