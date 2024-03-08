import keras
import numpy
from tensorflow.keras.utils import to_categorical

# cifar 불러오기
cifar = keras.datasets.cifar10.load_data()

# print(cifar)

(x_train, y_train), (x_test, y_test) = cifar
print(x_train.shape, x_test.shape)      # (50000, 32, 32, 3) (10000, 32, 32, 3) : 5000개의 이미지, 32*32 크기, 3채널
print(y_train.shape, y_test.shape)      # (50000, 1) (10000, 1) 50,000개의 이미지, 1차원 배열

# 목표 변수를 원-핫 인코딩
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)


# cifar 모델은 32*32 이미지 이기에 이미지 조절을 따로 하지 않아도 된다.

# 모델 정의
model = keras.Sequential([
    keras.layers.Input(shape=(32, 32, 3)),

    keras.layers.Conv2D(6, 5, 1, 'SAME', activation='relu'),
    keras.layers.MaxPool2D(2, 2),
    keras.layers.Conv2D(16, 5, 1, 'VALID', activation='relu'),
    keras.layers.MaxPool2D(2, 2),

    keras.layers.Flatten(),

    keras.layers.Dense(120, activation='relu'),
    keras.layers.Dense(84, activation='relu'),
    keras.layers.Dense(10, activation='softmax'),
])

# 모델 학습 설정
model.compile(optimizer=keras.optimizers.Adam(0.001),
              loss='categorical_crossentropy',
              metrics=['acc'])

# 모델 학습
model.fit(x_train, y_train, epochs=30, batch_size=100, verbose=2,
          validation_split=0.8)

# 모델 평가
print('acc :', model.evaluate(x_test, y_test, verbose=0))
