# linear, multiple      -> regression. 회귀
# logistic, softmax     -> regression  분류

import tensorflow.keras as keras

x = [[1, 2],
     [2, 1],
     [4, 5],
     [5, 4],
     [8, 9],
     [9, 8]]
y = [[3],
     [3],
     [9],
     [9],
     [17],
     [17]]

model = keras.Sequential()      #functional 은 다루지 않음
model.add(keras.layers.Dense(1))     # layer 1 개 추가 , (1) : 출력의 갯수 -> 데이터에 1개의 결과
# model.add(keras.layers.Dense(1))     # layer 1 개 추가

model.compile(optimizer=keras.optimizers.SGD(0.01),
              loss=keras.losses.mean_squared_error)

model.fit(x, y, epochs=10, verbose=2)       # epochs=5: 학습 5번
print(model.evaluate(x))

# 퀴즈
# 2시간 공부하고 7번 출석한 학생과
# 5시간 공부하고 1번 출석한 학생의 성적을 구하세요(predict)

print(model.predict(x))
print(model.predict([[1, 2],
                     [2, 1],
                     [4, 5],
                     [5, 4],
                     [8, 9],
                     [9, 8]]))
print(model.predict([[2, 7],
                     [5, 1],
                     ]))





















