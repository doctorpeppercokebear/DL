# quiz
# diabetes.csv file에 대해 동작하는 딥러닝 모델을 만들고
# 70%의 데이터로 학습하고 30%에 대해 정확도를 구하세요

import pandas as pd
import numpy as np
import tensorflow.keras as keras
from sklearn import preprocessing, model_selection
def read_diabetes():
    diabetes = pd.read_csv('data/diabetes.csv')
    print(diabetes)

    return diabetes.values[:, :-1], diabetes.values[:, -1:]

x, y = read_diabetes()
# print(x.shape, y.shape)

x = preprocessing.minmax_scale(x)       # 정규화

train_size = 500
# x_train, x_test = x[:train_size], x[train_size:]
# y_train, y_test = y[:train_size], y[train_size:]

# data = model_selection.Sql          # 일부 데이터 추출

data = model_selection.train_test_split(x, y, train_size=500)
x_train, x_test, y_train, y_test = data
print(x_train.shape, x_test.shape)
print(y_train.shape, y_test.shape)

model = keras.Sequential()
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.binary_crossentropy,
              metrics='acc')

model.fit(x, y, epochs=300, verbose=2,
          validation_data=(x_test, y_test))       # epochs=5: 학습 5번, validation loss 를 확인해서 학습을 더 할지 정한다.
print(model.evaluate(x, y, verbose=0))

p = model.predict(x_test, verbose=0)
print('acc : ', np.mean((p > 0.5) == y_test))




# print(df.head())        # 전처리 할게 없음
#
# # 모델 구축 x, y 로 나누면 된다. 비율은 7 : 3
# # x 값에 뭘 사용할 건지 y값에 어떤걸 예측할 건지 나눠야함  y 에 outcome -> 0 1 구분  -> 로지스틱 회귀?  나머지 전부 x
#
# x_columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiaberesPedigreeFunction', 'Age']
# y_columns = ['OUtcome']
#
# x = df.values[x_columns]
# y = df.values[y_columns]
#
# # 딥러닝 모델 구

