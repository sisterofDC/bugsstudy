import tensorflow as tf
import numpy as np
# print(tf.reduce_sum(tf.random.normal([1000, 1000])))
# this is baisc use of tensorflow,这里就简单的实现了一个使用阵列结构的一个函数



g = tf.Graph()
with g.as_default():
    x = tf.compat.v1.placeholder(dtype=tf.float32,shape=(None,2,3),name='x')
    x2 = tf.reshape(x, shape=(-1, 6),name='x2')
    xsum = tf.reduce_sum(x2, axis=0, name='col_sum')

with tf.compat.v1.Session(graph=g) as sess:
    x_array = np.arange(18).reshape(3, 2, 3)
    print(x_array)
    print(sess.run(x2, feed_dict={x:x_array}))

