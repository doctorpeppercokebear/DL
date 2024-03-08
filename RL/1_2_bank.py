'''
퀴즈
은행 영업 데이터셋에 대해
60%로 학습하고 20%로 대해 검증하고
최종적으로 나머지 20%에 대해 결과를 구하세요
bank.csv 파일로 마들어 보고, 이후 bank-full.csv 대해 결과를 확인

16개 입력 변수 1개의 출력 변수를 가지고 있다 마지막 y에 대해서 고객이 예금 상품을 가입 했는지에 대해서 출력하면 된다.
'''

import pandas
import numpy as np
import keras
import pandas as pd
from sklearn import preprocessing, model_selection

def make_xy():
    bank = pd.read_csv('data/bank.csv', sep=';')    # sep=';' 사용하면 ; 삭제 할 수 있음
    bank = pd.read_csv('data/bank-full.csv', sep=';')    # sep=';' 사용하면 ; 삭제 할 수 있음
    print(bank.head(10))

    bin = preprocessing.LabelBinarizer()
    y = bin.fit_transform(bank.y)

    # print(y[:5])

    bank.info()

    # 문자열 데이터를 원 핫 백터로 바꾸는 작업
    marital = bin.fit_transform(bank.marital)
    education = bin.fit_transform(bank.education)
    housing = bin.fit_transform(bank.housing)
    loan = bin.fit_transform(bank.loan)
    contact = bin.fit_transform(bank.contact)
    month = bin.fit_transform(bank.month)
    poutcome = bin.fit_transform(bank.poutcome)
    default = bin.fit_transform(bank.default)

    numbers = [
        bank.age, bank.balance, bank.day,
        bank.duration, bank.campaign, bank.pdays,
        bank.previous
    ]
    numbers = np.float32(numbers)       # (7, 4521)
    numbers = numbers.transpose()
    print(numbers.shape)

    x = np.hstack([
        numbers, marital, education, default,
        housing, loan, contact, month, poutcome
    ])

    print(x.shape)

    return x, y

def split_data(x, y):
    data = model_selection.train_test_split(x, y, train_size=0.8)
    x_total, x_test, y_total, y_test = data

    data = model_selection.train_test_split(x_total, y_total, train_size=0.75)
    x_train, x_valid, y_train, y_valid = data

    return x_train, y_train, x_valid, y_valid, x_test, y_test


'''
퀴즈
y 데이터의 비율에 맞춰서 데이터를 분활하세요
'''
def split_data_balanced(x, y):
    # yes, no = [], []
    # for i in range(len(y)):
    #     if y[i] == 1:
    #         yes.append(i)
    #     else:
    #         no.append(i)
    #
    # yes_x, yes_y = x[yes], y[yes]
    # no_x, no_y = x[no], y[no]
    # print(yes_x.shape, no_x.shape)  # (521, 36) (4000, 36)

    x_no = x[y[:, 0] == 0]
    y_no = y[y.reshape(-1) == 0]
    x_yes = x[y.reshape(-1) == 1]
    y_yes = y[y.reshape(-1) == 1]
    print(x_yes.shape, x_no.shape)  # (521, 36) (4000, 36)

    # bad
    # x1, y1, x2, y2, x3, y3 = split_data(x_no, y_no)
    # x4, y4, x5, y5, x6, y6 = split_data(x_yes, y_yes)
    #
    # x_train = np.vstack([x1, x4])
    # y_train = np.vstack([y1, y4])

    return split_data(np.vstack([x_no, x_yes]), np.vstack([y_no, y_yes]))




x, y  = make_xy()

# 스케일 진행
x = preprocessing.scale(x)

# 모델 학습
model = keras.Sequential([
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid'),        # 이진 분류에서 마지막 활성화 함수에 sigmoid를 사용한다.
])

model.compile(optimizer=keras.optimizers.Adam(0.001),
              loss = keras.losses.binary_crossentropy,
              metrics='acc')

model.fit(x, y, epochs=10, verbose=2, validation_data=(x_valid, y_valid), batch_size=64)
