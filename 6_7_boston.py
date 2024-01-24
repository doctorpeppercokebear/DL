import pandas as pd
import numpy as np
import tensorflow.keras as keras
from sklearn import preprocessing, model_selection

boston = pd.read_excel('data/boston.xls')
print(boston)

x = boston.values[:, :-2]
y = boston.values[:, -2:-1]

x = preprocessing.scale(x)

data = model_selection.train_test_split(x, y, train_size=500)
x_train, x_test, y_train, y_test = data

model = keras.Sequential()      #functional 은 다루지 않음
model.add(keras.layers.Dense(1))     # layer 1 개 추가 , (1) : 출력의 갯수 -> 데이터에 1개의 결과

model.compile(optimizer=keras.optimizers.SGD(0.01),
              loss=keras.losses.mean_squared_error)

model.fit(x_train, y_train, epochs=50, verbose=2)       # epochs=5: 학습 5번
print('mae : ', model.evaluate(x_test, y_test, verbose=0))

p = model.predict(x_test, verbose=0)                # p : 예측값
print('mae:', np.mean(np.abs(p - y_test)))


# def read_boston():
#     boston = pd.read_excel('data/boston.xls')
#     return boston.values[:, :-1], boston.values[:, -1]

# # Assign read_boston to x, y
# x, y = read_boston()
#
# # normalization
# x = preprocessing.minmax_scale(x)
# train_size = 500
#
# # Split learning data verification data
# data = model_selection.train_test_split(x, y, train_size=500)
# x_train, x_test, y_train, y_test = data
# print(x_train.shape, x_test.shape)
# print(y_train.shape, y_test.shape)
#
# # Model training
# model = keras.Sequential()
# model.add(keras.layers.Dense(1, activation='linear'))
#
# model.compile(optimizer=keras.optimizers.SGD(0.1),
#               loss='mean_squared_error',
#               metrics=['mse'])
#
# model.fit(x_train, y_train, epochs=300, verbose=2,
#           validation_data=(x_test, y_test))
#
# # Model evaluation
# result = model.evaluate(x_test, y_test, verbose=0)
# print("Mean Squared Error:", result[1])
