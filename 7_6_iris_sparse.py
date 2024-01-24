# 퀴즈
# iris sparse sparkling color scheme
import pandas as pd
import tensorflow.keras as keras
import numpy as np
from sklearn import preprocessing  # 올바른 모듈명 사용

def read_iris():
    iris = pd.read_csv('data/iris.csv')

    x = iris.values[:, :-1]
    variety = iris.values[:, -1]  # 1차원

    enc = preprocessing.LabelEncoder()
    y = enc.fit_transform(variety)
    print(y[:5])

    return np.float32(x), y, enc  # 'classes_' 속성을 직접 사용하지 않고, 전체 LabelEncoder 객체 반환

x, y, encoder = read_iris()
print(x.shape, y.shape)

model = keras.Sequential()
model.add(keras.layers.Dense(3, activation='softmax'))

model.compile(optimizer=keras.optimizers.SGD(0.01),
              loss=keras.losses.sparse_categorical_crossentropy,
              metrics='acc')

model.fit(x, y, epochs=50, verbose=2)

np.set_printoptions(linewidth=1000)

# 퀴즈
# 예측한 결과 중에서 틀린 데이터만 출력하세요
# 정답과 오답까지 출력합니다.

p = model.predict(x, verbose=0)
p = np.argmax(p, axis=1)

print(y)
print(p)

bools = (p != y)  # 오분류된 샘플의 인덱스를 찾기 위한 불리언 배열
wrong = x[bools]

print(wrong)

y_wrong, p_wrong = y[bools], p[bools]       # 참 인 값만 출력
print(y_wrong)
print(p_wrong)

# 이제 encoder 객체의 inverse_transform 메서드를 사용하여 실제 클래스 레이블로 변환
print(encoder.inverse_transform(y_wrong))
print(encoder.inverse_transform(p_wrong))

for dd, pp, yy in zip(wrong, encoder.inverse_transform(p_wrong), encoder.inverse_transform(y_wrong)):
    print(dd, pp, yy)
print('-'*50)

# print(p_arg)
#
# # 오분류된 샘플 찾기
# # np.where(p_arg != y) 는 NumPy에서 배열의 특정 조건을 만족하는 요소의 인덱스를 찾는 함수
# incorrect_indices = np.where(p_arg != y)[0]     # 모델의 예측 결과 'p_arg'와 실제 클래스 y가 다른 경우의 인덱스를 찾는다.
#
# # 정확한 분류와 오분류된 샘플 출력
# print("정확한 분류:")
# correct_indices = np.where(p_arg == y)[0]
# print(correct_indices)
#
# print("오분류:")
# print(incorrect_indices)
#
# # 오분류된 샘플에 대한 예측 결과 출력
# incorrect_predictions = p[incorrect_indices]
# print("오분류된 샘플의 예측 결과:")
# print(incorrect_predictions)
#
# read_iris()