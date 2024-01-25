
# 퀴즈
# car.data 파일레 대해 동작하는 모델을 만드세요
# 70% 로 학습하고 30%에 대해 결과를 보여주세요
import pandas as pd
import numpy as np
import tensorflow.keras as keras
from sklearn import preprocessing, model_selection

# car.data 파일을 읽는 함수
def read_car():
    car = pd.read_csv('data/car.data', header=None)
    print(car)

    features = []
    enc = preprocessing.LabelEncoder()
    for i in range(6):
        # print(car.values[:, i])
        result = enc.fit_transform(car.values[:, i])
        # print(result)
        features.append(result)      # 2차원

    x = np.int32(features)      # 넘파이 배열로 변경
    print(x.shape)

    x = x.transpose()       # 행과 열이 변경되었기에 transpose를 이용해서 변경
    # x = x.T       # 짧아서 많이 사용한다.
    print(x.shape)

    y = enc.fit_transform(car.values[:, -1])
    return x, y

def read_car_2():
    car = pd.read_csv('data/car.data', header=None)

    enc =preprocessing.LabelEncoder()
    features = [enc.fit_transform(car.values[:, i]) for i in range(6)]

    return  np.int32(features).T, enc.fit_transform(car.values[:, -1])


x, y = read_car()
print(x.shape, y.shape)

read_car()
read_car_2()
# # 정규화
# scaler = preprocessing.scale(x)
#
# # 레이블을 숫자로 변환
# encoded_x, encoder_x = label_binarizer(x)
# encoded_y, encoder_y = label_binarizer(y)
#
# # 모델 생성
model = keras.Sequential()
model.add(keras.layers.Dense(4, activation='softmax'))

model.compile(optimizer=keras.optimizers.SGD(0.01),
              loss=keras.losses.sparse_categorical_crossentropy,
              metrics='acc')

model.fit(x, y, epochs=100, verbose=2)

