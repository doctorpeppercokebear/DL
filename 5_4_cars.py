import pandas as pd
import tensorflow.keras as keras  # tensorflow.keras를 사용
from tensorflow.keras.callbacks import TensorBoard
import matplotlib.pyplot as plt

# 퀴즈
# cars.cav 파일에 대한 딥러닝 모델 구축
# 속도가 30 또는 50 일 때의 제동 거리 찾기
def read_cars():
    cars = pd.read_csv('data/cars.csv', index_col=0)
    # print(cars)
    # print(cars.values)


    x = cars.speed.values.reshape(-1, 1)  # 시리즈
    y = cars['dist'].values.reshape(-1, 1)
    # print(x.shape, y.shape)

    return x, y

x, y = read_cars()

# x = cars.values[:, 1:-1]
# y = cars.values[:, :-1]
# print(x.shape, y.shape)

model = keras.Sequential()  # 함수형은 다루지 않음
model.add(keras.layers.Dense(1))  # 1개의 레이어 추가, (1): 데이터에서의 결과값 개수 -> 1개의 결과값
# model.add(keras.layers.Dense(1)) # 1개의 레이어 추가

model.compile(optimizer=keras.optimizers.SGD(0.001),  # SGD 옵티마이저 사용
              loss=keras.losses.mse)  # 평균 제곱 오차 (MSE) 손실 함수 사용

model.fit(x, y, epochs=300, verbose=2)  # epochs=10: 학습 횟수 10회, verbose = 0, 1, 2 -> 출력 창 조절

print('-'*50)
# 퀴즈
# 속도가 30과 50일 떄의 제동거리를 구하고
# 예측 결과를 그래프로 그려주세요

p = model.predict([[30],[50]], verbose=0)
print(p)

# plt.plot(read_cars['speed'], pre)
#
# plt.show()

p0, p1, p2 = p[0, 0], p[1, 0], p[2, 0]

plt.plot(x, y, 'ro')
plt.plot([0, 30, 50], [0, p1, p2], 'g')
plt.plot([0, 30], [p0, p1], 'k')
plt.show
