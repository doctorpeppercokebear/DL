import tensorflow.keras as keras
import numpy as np

# 퀴즈
# onehot 데이터를 sparse 버전으로 수정하세요
x = [[1, 2],    # c
     [2, 1],
     [4, 5],    # b
     [5, 4],
     [8, 9],    # a
     [9, 8]]
y = [2, 2, 1, 1, 0, 0]


model = keras.Sequential()
model.add(keras.layers.Dense(3, activation='softmax'))          # 활성화 함수 : softmax 사용 -> 합계 1

model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.sparse_categorical_crossentropy,        # 원 핫 인코딩으로 되어 있지 않으니 원 핫 인코딩으로 바꿔줌
              metrics='acc')

model.fit(x, y, epochs=200, verbose=2)       # epochs=5: 학습 5번
# print(model.predict(x, verbose=1))

p = model.predict(x, verbose=0)
print(p)

p_arg = np.argmax(p, axis=1)
print(p_arg)