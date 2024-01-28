# 8_4 callback      내가 호출할 수 없다.

import tensorflow.keras as keras
from sklearn import preprocessing, model_selection
import matplotlib.pyplot as plt
from tensorflow.python.client import device_lib

mnist = keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = mnist

x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)

# 정규화
x_train = x_train / 255

x_test = x_test / 255

#
model = keras.Sequential([
        keras.layers.Dense(10, activation='softmax'),
    ])

model.compile(optimizer=keras.optimizers.RMSprop(0.001),
                  loss=keras.losses.sparse_categorical_crossentropy,
                  metrics='acc')

early_stopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)

reduce_lr = keras.callbacks.ReduceLROnPlateau(factor=0.2, patience=3)

checkpoints = keras.callbacks.ModelCheckpoint(filepath='model/mnist_{epoch:02d}-{val_loss:.5f}_model.keras',
                                              save_best_only=True,      # 가장 좋은 모델만 저장
                                              verbose=1)

history = model.fit(x_train, y_train, epochs=30, verbose=2, batch_size=100,
            validation_data=(x_test, y_test),
            callbacks=[checkpoints])

# print(history.history )
# print(history.history.keys() )  # ['loss', 'acc', 'mae', 'val_loss', 'val_acc', 'val_mae']

# 퀴즈
# history 에 들어있는 값을 그래프로 그려보세요
# indices = range(1, 11)
#
# plt.title('loss')
# plt.plot(indices, history.history['loss'], 'r')
# plt.plot(indices, history.history['val_loss'], 'g')
#
# plt.figure()
# plt.title('accuracy')
# plt.plot(indices, history.history['acc'], 'r')
# plt.plot(indices, history.history['val_acc'], 'g')
# plt.show()
