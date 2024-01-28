from tensorflow.keras.datasets import mnist
import tensorflow.keras as keras
import numpy as np
# import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
# train data validation data split
(x_train, y_train), (x_valid, y_valid) = mnist.load_data()

# data 살펴보기
print(x_train.shape)    # (60000, 28, 28)

print(x_valid.shape)    # (10000, 28, 28) -> 28 x 28 사이즈 2D array

print(x_train.dtype)    # uint8

print(x_train.min())    # 0

print(x_train.max())    # 255

print('-'* 30)

# 이미지 평탄화
x_train = x_train.reshape(60000, 784)       # 각 이미지를 784의 연속픽셀(28*28)로 이루어진 단일 어레이로 재구성
x_valid = x_valid.reshape(10000, 784)

# 평탄화 확인
print(x_train.shape)    # (60000, 784)

print('-'* 30)

# 이미지 데이터 정규화
# 정수 값을 0에서 1 사이의 부동 소수점 값으로 변환하는 걸 정규화라고 한다.

x_train = x_train / 255
x_valid = x_valid / 255

# print(x_train.shape)

print(x_train.dtype)

print(x_train.min())

print(x_train.max())

print('-'* 30)

# 레이블 범주 인코딩

num_categories = 10

y_train = keras.utils.to_categorical(y_train, num_categories)
y_valid = keras.utils.to_categorical(y_valid, num_categories)

print(y_train[0:9])

# 모델 생성

# 모델 인스턴스화
model = Sequential()

# 입력 레이어 생성
model.add(Dense(units=512, activation='relu', input_shape=(784,)))

# 숨겨진 레이어 생성
model.add(Dense(units= 512, activation='relu'))

# 출력 레이어 생성
# softmax : 각 레이어의 값이 0에서 1 사이의 확률이 되도록 하고 레이어의 모든 출력이 1에 추가되로록 하는 활성 함수
model.add(Dense(units = 10, activation='softmax' ))

#  모델 요약
print(model.summary())

# 모델 컴파일
# 트레이닝 중 모델에서 성능을 파악하는 데 사용되는 손실 함수를 지정
# 트레이닝 동안 accury도 추적하도록 지정
model.compile(loss='categorical_crossentropy', metrics=['accuracy'])

# 모델 트레이닝
# fit 메서드를 이용

history = model.fit(
    x_train, y_train, epochs=5, verbose=1, validation_data=(x_valid, y_valid)
)














