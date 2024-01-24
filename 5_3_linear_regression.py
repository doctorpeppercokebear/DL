# linear, multiple      -> regression. 회귀
# logistic, softmax     -> regression  분류

import tensorflow.keras as keras

x = [[1],
     [2],
     [3]]
y = [[1],
     [2],
     [3]]

model = keras.Sequential()      #functional 은 다루지 않음
model.add(keras.layers.Dense(1))     # layer 1 개 추가 , (1) : 출력의 갯수 -> 데이터에 1개의 결과
# model.add(keras.layers.Dense(1))     # layer 1 개 추가

model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.mean_squared_error)

model.fit(x, y, epochs=5)       # epochs=5: 학습 5번
print(model.evaluate(x))