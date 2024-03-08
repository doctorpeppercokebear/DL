
'''
퀴즈
mnist 데이터에 대해 동작하는 RNN 모델을 만드세요
'''

import keras
import numpy

# 데이터 불러오기
mnist = keras.datasets.mnist.load_data()

# x_train, y_train, test  값 불러오기
# (60000, 28, 28) (10000, 28, 28)
(x_train, y_train), (x_test, y_test) = mnist

print(x_train.shape, x_test.shape)

x_train = x_train / 255
x_test = x_test /255


'''
1번
'''
# x_train = x_train.reshape(-1, 784) # 1차원 기본 모델
# x_test = x_test.reshape(-1, 784)
#
# model = keras.Sequential([
#     keras.layers.Dense(10, activation='softmax')
# ])
#
# model.compile(optimizer=keras.optimizers.Adam(0.001),
#               loss = keras.losses.sparse_categorical_crossentropy,
#               metrics='acc')
#
# model.fit(x_train, y_train, epochs=10, batch_size=100,
#           verbose=2, validation_data=(x_test, y_test))


'''
2번  CNN
 loss: 0.0757 - acc: 0.9769 - val_loss: 0.0732 - val_acc: 0.9773 - 2s/epoch - 3ms/step
'''
# x_train = x_train.reshape(-1, 28, 28, 1) # 3차원 cnn
# x_test = x_test.reshape(-1, 28, 28, 1)
#
# model = keras.Sequential([
#     keras.layers.Conv2D(6, 3, 1, 'same', activation='relu'),
#     keras.layers.MaxPool2D(2, 2),
#     keras.layers.Conv2D(6, 3, 1, 'same', activation='relu'),
#     keras.layers.MaxPool2D(2, 2),
#     keras.layers.Flatten(),
#     keras.layers.Dense(10, activation='softmax')
# ])
#
# model.compile(optimizer=keras.optimizers.Adam(0.001),
#               loss = keras.losses.sparse_categorical_crossentropy,
#               metrics='acc')
#
# model.fit(x_train, y_train, epochs=10, batch_size=100,
#           verbose=2, validation_data=(x_test, y_test))


'''
3번 모델 RNN
loss: 0.5230 - acc: 0.8371 - val_loss: 0.4810 - val_acc: 0.8537
'''
x_train = x_train.reshape(-1, 28, 28)  # 2차원은 RNN
x_test = x_test.reshape(-1, 28, 28)

model = keras.Sequential([
    keras.layers.SimpleRNN(16),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer=keras.optimizers.Adam(0.001),
              loss = keras.losses.sparse_categorical_crossentropy,
              metrics='acc')

model.fit(x_train, y_train, epochs=10, batch_size=100,
          verbose=2, validation_data=(x_test, y_test))



