import gzip
import os
import struct
import tempfile
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from keras.utils.np_utils import *
import tensorflow.lite.python.lite
from tensorflow import keras
from tensorflow import lite
from keras.models import Sequential
from keras.models import save_model
from keras.layers import Dense
from keras.layers import Activation
from tensorflow.keras import optimizers
from tensorflow.keras.models import load_model

# 得到训练集
path = 'E:\TensorFlowstudy\\begin\\mnist'


def load_mnist_train(path, kind='train'):
    labels_path = os.path.join(path, '%s-labels.idx1-ubyte' % kind)
    images_path = os.path.join(path, '%s-images.idx3-ubyte' % kind)
    with open(labels_path, 'rb') as lbpath:
        magic, n = struct.unpack('>II', lbpath.read(8))
        labels = np.fromfile(lbpath, dtype=np.uint8)
    with open(images_path, 'rb') as imgpath:
        magic, num, rows, cols = struct.unpack('>IIII', imgpath.read(16))
        images = np.fromfile(imgpath, dtype=np.uint8).reshape(len(labels), 784)
        # # 首先就进行归一化
        # images = ((images/255.) - .5) *2
    return images, labels


def load_mnist_test(path, kind='t10k'):
    labels_path = os.path.join(path, '%s-labels.idx1-ubyte' % kind)
    images_path = os.path.join(path, '%s-images.idx3-ubyte' % kind)
    with open(labels_path, 'rb') as lbpath:
        magic, n = struct.unpack('>II', lbpath.read(8))
        labels = np.fromfile(lbpath, dtype=np.uint8)
    with open(images_path, 'rb') as imgpath:
        magic, num, rows, cols = struct.unpack('>IIII', imgpath.read(16))
        images = np.fromfile(imgpath, dtype=np.uint8).reshape(len(labels), 784)
        # # 首先就进行归一化
        # images = ((images / 255.) - .5) * 2
    return images, labels


# fig = plt.figure(figsize=(8, 8))
# fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
# for i in range(30):
#     images = np.reshape(train_images[i], [28, 28])
#     ax = fig.add_subplot(6, 5, i + 1, xticks=[], yticks=[])
#     ax.imshow(images, cmap=plt.cm.binary, interpolation='nearest')

# plt.show()

if __name__ == '__main__':
    X_train, y_train = load_mnist_train(path)
    X_test, y_test = load_mnist_test(path)
    # print(X_train.shape[0], X_train.shape[1])
    # print(X_test.shape[0], X_test.shape[1])



    # 这里把所有的训练集变为[-1.1]之间
    # -1. - 1. - 0.97647059 - 0.85882353 - 0.85882353 - 0.85882353
    # -0.01176471 0.06666667 0.37254902 - 0.79607843 0.30196078 1.
    # 0.9372549 - 0.00392157 - 1. - 1. - 1. - 1.



    fig = plt.figure(figsize=(8, 8))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
    for i in range(5):
        images = np.reshape(X_train[i], [28, 28])
        ax = fig.add_subplot(6, 5, i + 1, xticks=[], yticks=[])
        ax.imshow(images, cmap=plt.cm.binary, interpolation='nearest')
        ax.text(0, 7, str(y_train[i]))
    plt.show()



    # mean()函数的功能是求取平均值

    mean_vals = np.mean(X_train,axis=0)

    # std()计算沿指定轴的标准差。返回数组元素的标准差
    std_val =np.std(X_train)


    #将样本归一化，及样本x-y/z x为样本 y为样本均值 z 为标准方差
    X_train_centered = (X_train - mean_vals)/std_val
    X_test_centered = (X_test - mean_vals)/std_val


    print(X_train_centered[0].reshape(28,28))

    print(X_train_centered.shape,y_train.shape)
    print(X_test_centered.shape,y_test.shape)


    # 为numpy和tensorflow设置随机种子

    np.random.seed(115)
    tf.random.set_seed(115)

    # #设置标签，需要把分类标签转换为独热格式 将单词表示为向量的第一种方式是创建独热码
    # y_train_onehot = to_categorical(y_train)
    # print(y_train_onehot[:3])
    #
    # model =Sequential()
    # # 设置层数
    # model.add(Dense(units=50,input_dim=X_train_centered.shape[1],kernel_initializer='glorot_uniform',bias_initializer='zeros',activation='tanh'))
    #
    # model.add(Dense(units=50,input_dim=50,kernel_initializer='glorot_uniform',bias_initializer='zeros',activation='tanh'))
    #
    # model.add(Dense(units=y_train_onehot.shape[1],input_dim=50,kernel_initializer='glorot_uniform',bias_initializer='zeros',activation='softmax'))
    #
    # sgd_optimizer = optimizers.SGD(learning_rate=0.001,decay=1e-7,momentum=.9)
    #
    # model.compile(optimizer=sgd_optimizer,loss='categorical_crossentropy')
    #
    # # 开始训练
    # history = model.fit(X_train_centered,y_train_onehot,batch_size=64,epochs=50,verbose=1,validation_split=0.1)


    load_model = load_model("./savemodel/handwrite.h5")


    # y_train_pred = model.predict(X_train_centered)


    y_train_load_pred = load_model.predict(X_train_centered)
    print(y_train_load_pred[:5])





    # correct_preds =np.sum(y_train == y_train_pred,axis=0)
    # train_acc = correct_preds / y_train.shape[0]
    #
    # print(train_acc*100)




    # # 将训练的模型进行保存
    # keras_file ="./savemodel/handwrite.h5"
    # save_model(model,keras_file)
    # converter = lite.TFLiteConverter.from_keras_model(model)
    # tfmodel = converter.convert()
    # open("./savemodel/handwrite.tflite", "wb").write(tfmodel)
    # 
    # # 查看训练模型的的输入和输出
    # interpreter = tf.lite.Interpreter(model_path='./savemodel/handwrite.tflite')
    # interpreter.allocate_tensors()
    # 
    # print(interpreter.get_input_details())
    # print(interpreter.get_output_details())
