
# 퀴즈
# iris 파일에 대해서 sparse 버전의 모델을 구축하세요
import pandas as pd
import tensorflow.keras as keras
import numpy as np
from sklearn import preprocessing

def read_iris():
    iris = pd.read_csv('data/iris_onhot.csv')
    x = iris.values[:, :-1]
    variety = iris.values[:, -1]            # 1차원

    enc = preprocessing.LabelEncoder()      # enc : encoder
    y = enc.fit_transform(variety)
    print(y[5])
    exit()

    return x, y

x, y = read_iris()
print(x.shape, y.shape)

model = keras.Sequential()
model.add(keras.layers.Dense(3, activation='softmax'))

model.compile(optimizer=keras.optimizers.SGD(0.01),
              loss=keras.losses.sparse_categorical_crossentropy,            # sparse_categorical_crossentropy 로 변경
              metrics='acc')

model.fit(x_train, y_train, epochs=50, verbose=2,
          validation_data=(x_texst, y_texst))

p = model.predict(x, verbose=0)
print(p)

p_arg = np.argmax(p, axis=1)
print(p_arg)

read_iris()