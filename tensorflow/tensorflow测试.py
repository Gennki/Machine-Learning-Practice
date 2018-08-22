import tensorflow as tf
from mnist import input_data
import matplotlib.pyplot as plt
import numpy as np

mnist = input_data.read_data_sets("./mnist")

X_train = tf.placeholder(tf.float32, [None, 784])
y_train = tf.placeholder(tf.float32, [None, 1])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(X_train, W) + b)

cross_entropy = -tf.reduce_sum(y_train * tf.log(y))
train = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        batch_xs = np.array(batch_xs).reshape(-1, 784)
        batch_ys = np.array(batch_ys).reshape(-1, 1)
        print(batch_xs.shape, batch_ys.shape)

        sess.run(train, feed_dict={X_train: batch_xs, y_train: batch_ys})
        if i % 50 == 0:
            print(sess.run(cross_entropy))
