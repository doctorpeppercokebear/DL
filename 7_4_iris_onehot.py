# iris_onthot 파일에 대해 모델을 구축하고
# 70%로 학습하고 30%에 대해 정확도를 구하세요
# train_test_split 사용금지
# 강사님 코드 가져와 함
import pandas as pd
import numpy as np
import tensorflow.keras as keras
from sklearn import preprocessing, model_selection

def read_iris():
    iris = pd.read_csv('data/iris_onhot.csv')
    # x = iris.values[:, :-3]
    # y = iris.values[:, -3:]

    values = iris.values[:]
    np.random.shuffle(values)

    x = values[:, :-3]
    y = values[:, -3:]

    return x, y

x, y = read_iris()
print(x.shape, y.shape)

x_train, x_texst = x[:105], x[105:]
y_train, y_texst = y[:105], y[105:]

model = keras.Sequential()
model.add(keras.layers.Dense(3, activation='softmax'))

model.compile(optimizer=keras.optimizers.SGD(0.01),
              loss=keras.losses.categorical_crossentropy,
              metrics='acc')

model.fit(x_train, y_train, epochs=50, verbose=2,
          validation_data=(x_texst, y_texst))


