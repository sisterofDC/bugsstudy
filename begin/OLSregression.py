import os
import tempfile
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
from tensorflow import lite

# 相当于直接用的tensorflow v1 的代码,需要重构为v2的代码

X_train = np.arange(10).reshape((10, 1))
y_train = np.array([1.0, 1.3, 3.1, 2.0, 5.0, 6.3, 6.6, 7.4, 8.0, 9.0])



class OLS(object):
    def __init__(self, x_dim, learning_rate=0.01, random_seed=None):
        self.x_dim = x_dim
        self.learning_rate = learning_rate
        self.g = tf.Graph()

        # 定义学习率和使用组件

        with self.g.as_default():
            tf.compat.v1.set_random_seed(random_seed)
            self.build()
            self.init_op = tf.compat.v1.global_variables_initializer()

    def build(self):
        self.X = tf.compat.v1.placeholder(dtype=tf.float32, shape=(None, self.x_dim), name='X_input')
        self.y = tf.compat.v1.placeholder(dtype=tf.float32, shape=None, name='y_input')
        print(self.X)
        print(self.y)
        # 设置权重和偏执
        w = tf.Variable(tf.zeros(shape=(1)), name='weight')
        b = tf.Variable(tf.zeros(shape=(1)), name='bias')
        print(w)
        print(b)
        # 定义回归模型 z=w*x+b
        self.z_net = tf.squeeze(w * self.X + b, name="bias")
        print(self.z_net)
        # 定义平方差均值
        sqr_errosrs = tf.square(self.y - self.z_net, name='sqr_errors')
        print(sqr_errosrs)
        # 损失函数

        self.mean_cost = tf.reduce_mean(sqr_errosrs, name='mean_cost')
        # 梯度下降
        optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=self.learning_rate,
                                                                name='GradientDescent')
        # 最小化损失
        self.optimizer = optimizer.minimize(self.mean_cost)


# 开始运行

# 看每一个梯度下降的过程
def train_linreg(sess, model, X_train, y_train, num_epochs=10):
    sess.run(model.init_op)
    train_costs = []
    for i in range(num_epochs):
        cost = sess.run([model.optimizer, model.mean_cost], feed_dict={model.X: X_train, model.y: y_train})
        train_costs.append(cost)
    return train_costs


# 测试集

def predict_linreg(sess, model, X_test):
    y_predict = sess.run(model.z_net, feed_dict={model.X: X_test})
    return y_predict


if __name__ == '__main__':
    linermodel = OLS(x_dim=X_train.shape[1], learning_rate=0.01)

    sess = tf.compat.v1.Session(graph=linermodel.g)

    train_costs = train_linreg(sess=sess, model=linermodel, X_train=X_train, y_train=y_train)

    plt.plot(range(1, len(train_costs) + 1), train_costs)
    plt.tight_layout()
    plt.xlabel('epochs')
    plt.ylabel('cost')
    plt.show()

    plt.scatter(X_train, y_train, marker='s', s=50, label='training')
    plt.plot(range(X_train.shape[0]), predict_linreg(sess=sess, model=linermodel, X_test=X_train))
    plt.legend()
    plt.show()

# 这里好像自定义的还要写call函数
    # saved_model_dir= "E:\\TensorFlowstudy\savemodel"
    # tf.saved_model.save(linermodel,saved_model_dir)
    # converter = lite.TFLiteConverter.from_keras_model(linermodel)
    # tfmodel = converter.convert()
    # open("linear.tflite","wb").write(tfmodel)

