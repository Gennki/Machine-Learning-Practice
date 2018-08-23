import tensorflow as tf

# 构造图(Graph)
# 用一个线性方程的例子 y = W * x + b
W = tf.Variable(2.0, dtype=tf.float32, name="Weight")
b = tf.Variable(1.0, dtype=tf.float32, name="Bias")
x = tf.placeholder(dtype=tf.float32, name="Input")
with tf.name_scope("Output"):  # 输出的命名空间
    y = W * x + b

# 定义图保存的路径
path = "../log"

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    tf.summary.FileWriter(path, sess.graph)  # 保存图
    print(sess.run(y, feed_dict={x: 3.0}))

# 假设当前路径和log文件夹同一级,打开图的命令为tensorboard --logdir ./log
