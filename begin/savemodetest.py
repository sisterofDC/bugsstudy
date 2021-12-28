import os
import tempfile
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import tensorflow.lite.python.lite
from tensorflow import keras
from tensorflow import lite
from keras.models import Sequential
from keras.models import save_model
from keras.layers import Dense
from keras.layers import Activation

X_train = np.arange(10).reshape((10, 1))
y_train = np.array([1.0, 1.3, 3.1, 2.0, 5.0, 6.3, 6.6, 7.4, 8.0, 9.0])

model = Sequential([Dense(units=1,input_shape=[1]),Dense(units=1,input_shape=[1])])
model.compile(optimizer='sgd',loss='mean_squared_error')

model.fit(x=X_train,y=y_train,epochs=10)

print(model.predict([10]))

keras_file ="./savemodel/linear.h5"

save_model(model,keras_file)
converter = lite.TFLiteConverter.from_keras_model(model)
tfmodel = converter.convert()
open("./savemodel/linear.tflite","wb").write(tfmodel)
