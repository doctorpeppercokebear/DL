import tensorflow.keras as keras

x = [[1, 2],    # 탈락
     [2, 1],
     [4, 5],    # 통과
     [5, 4],
     [8, 9],
     [9, 8]]
y = [[0],
     [0],
     [1],
     [1],
     [1],
     [1]]

# model = keras.Sequential()      #functional 은 다루지 않음
# model.add(keras.layers.Dense(1, activation='sigmoid'))     # layer 1 개 추가 , (1) : 출력의 갯수 -> 데이터에 1개의 결과
# # model.add(keras.layers.Activation('sigmoid'))
#
# model.compile(optimizer=keras.optimizers.SGD(0.1),
#               loss=keras.losses.binary_crossentropy,
#               metrics='acc')

model = keras.Sequential()
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.binary_crossentropy,
              metrics='acc')

model.fit(x, y, epochs=300, verbose=2)       # epochs=5: 학습 5번
print(model.predict(x, verbose=1))

# quiz
# 예측한 결과에 대해 정확도를 구하세요
p_bool = (p > 0.5)
print(p_bool)

p_int = np.int32(p_bool)
print(p_int)

equals = (p_int == y)
print(equals)
print('acc : ', np.mean(equals))
print('acc : ', np.mean(p_bool == y))
