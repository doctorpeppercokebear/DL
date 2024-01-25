# 8_2_multi_layers.py
import tensorflow.keras as keras
from sklearn import preprocessing, model_selection

mnist = keras.datasets.mnist.load_data()
print(len(mnist))
print(len(mnist[0]))

(x_train, y_train), (x_test, y_test) = mnist
print(x_train.shape, x_test.shape)
print(y_train.shape, y_test.shape)

x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)

print(set(y_train))


# (60000, 28*28)   피쳐 : 28*28 -> 픽셀

# 퀴즈
# 스케일링 해보세요
# 이미지는 스케일링 무조건 해야한다.

# 아래 코드로 실전에서 사용하면 따로 공부하기에 큰일난다.
# x_train = preprocessing.minmax_scale(x_train)
# x_test = preprocessing.minmax_scale(x_test)

# # 이런식으로 스케일 해야한다.
# # 스케일링을 위한 MinMaxScaler 객체 생성
# scaler = preprocessing.MinMaxScaler()
#
# # 스케일링을 위해 훈련 데이터에 fit
# scaler.fit(x_train)
#
# # 훈련 데이터와 테스트 데이터에 스케일 적용
# x_train = scaler.transform(x_train)
# x_test = scaler.transform(x_test)


# #  이미지 처리는 아래 코드를 사용하낟.
#
x_train = x_train / 255         # 0 과 1 사이로 전환 컬러 흑백 작용 가능
x_test = x_test / 255


# print(set(y_train))
# 성능을 높이는 방법 레이어를 넓게 높게 만든다.  -> 데이터에 따라서 적용해보면서 적용
# layer를 연결할 때는 activation funtion 을 사용해야 한다.
# (60000, 10) = (60000, 784) @ (784, 10)  + 10 (바이어스)-> 웨이트 갯수 7840 + 10 + 7850

model = keras.Sequential()
# (?, 512) = (?, 784) @ (784, 512)   784 : 피처갯수 512 클래스 갯수
model.add(keras.layers.Dense(512, activation='relu'))           # layer 과의 연결은 relu 을 사용한다. 웨이트 갯수
# (?, 256) = (?, 512) @ (512, 256)  512 : 피처 갯수 256 : 클래스 갯수
model.add(keras.layers.Dense(256, activation='relu'))
# (?, 256) = (?, 256) @ (256, 256)
model.add(keras.layers.Dense(256, activation='relu'))
# (?, 128) = (?, 256) @ (256, 128)
model.add(keras.layers.Dense(128, activation='relu'))
# (?, 10) = (?, 128) @ (128, 10)
model.add(keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer=keras.optimizers.Adam(0.001),                   # Adam, RMprop  -> 둘 다 사용해봐야 한다. Adam을 사용하는게 좋다.
              loss=keras.losses.sparse_categorical_crossentropy,            # 원 핫 인코딩 이 아니기에 sparse 사용
              metrics='acc')

model.fit(x_train, y_train, epochs=10, verbose=2,
          validation_data=(x_test, y_test))

model.summary()