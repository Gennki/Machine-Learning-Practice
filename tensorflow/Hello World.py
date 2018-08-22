# -*- coding:UTF-8 -*-
import tensorflow as tf

# const = tf.constant("Hello World")
# with tf.Session() as sess:
#     print(sess.run(const))

a = tf.constant(2)
b = tf.constant(3)
c = tf.multiply(a, b)
d = tf.add(c, 1)
with tf.Session() as sess:
    print(sess.run(d))
