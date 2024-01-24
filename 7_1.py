import pandas as pd
import numpy as np
import tensorflow.keras as keras
from sklearn import preprocessing, model_selection

# Load model, # specify x and y
def read_wdvc():
    wdbc = pd.read_csv('data/wdbc.data', header=None, index_col=0)
    diagnose = wdbc.values[:, 0]
    x = wdbc.values[:, 1:]
    print(diagnose.shape, x.shape)
    print(diagnose[:5])

    enc = preprocessing.LabelEncoder()
    y = enc.fit_transform(diagnose)
    print(y[:5])

    print(wdbc.values.dtype)
    print(x.dtype, y.dtype)

    return np.float32(x), y.reshape(-1)

x, y = read_wdvc()
print(x.shape, y.shape)

# 정규화
scaler = preprocessing.scale(x)

# x, y 데이터 분리
data = model_selection.train_test_split(x, y, test_size=0.3)  # test_size를 0.3 또는 다른 적절한 값으로 변경
x_train, x_test, y_train, y_test = data

# 모델 구성
model = keras.Sequential()

model.add(keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer=keras.optimizers.SGD(0.01),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 모델 학습
model.fit(x_train, y_train, epochs=300, verbose=2)
print('acc : ', model.evaluate(x_test, y_test))
