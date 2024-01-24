import tensorflow.keras as keras
import numpy as np

x = [[1, 2],    # c
     [2, 1],
     [4, 5],    # b
     [5, 4],
     [8, 9],    # a
     [9, 8]]
y = [[0, 0, 1],
     [0, 0, 1],
     [0, 1, 0],
     [0, 1, 0],
     [1, 0, 0],
     [1, 0, 0]]


model = keras.Sequential()
model.add(keras.layers.Dense(3, activation='softmax'))          # 활성화 함수 : softmax 사용 -> 합계 1

model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.categorical_crossentropy,
              metrics='acc')

model.fit(x, y, epochs=300, verbose=2)       # epochs=5: 학습 5번
# print(model.predict(x, verbose=1))

p = model.predict(x, verbose=0)
print(p)

# # sample = x_test[:1]
# value = '0.00632,18,2.31,0,0.538,6.575,65.2,4.09,1,296,15.3,396.9,4.98'
# smape = [[float]]

# 퀴즈
# 예측한 결과에 대해 정확도를 구하세요
# p_bool = (p > 0.5)
# print(p_bool)
#
# p_int = np.int32(p_bool)
# print(p_int)
#
# equals = (p_int == y)
# print(equals)
# print('acc : ', np.mean(equals))
# print('acc : ', np.mean(p_bool == y))

# 강사님 코드
p_arg = np.argmax(p, axis=1)       # 0: 수직, 1 : 수평
print(p_arg)
print(y_arg)

print('acc : ', np.mean(p_arg == y_arg))
