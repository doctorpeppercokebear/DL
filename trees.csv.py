# 퀴즈
# trees.csv 파일을 읽어서
# Girth 와 Height 로 Volume을 예측하는 모델을 만드세요
# Girth가 10이고 Height가 70일 떄와
# Girth가 15이고 Height가 80일 때의 Volume을 구하세요

import pandas as pd
import tensorflow.keras as keras
import numpy as np

# tree = pd.read_csv('data/trees.csv')
#
# x = tree[['Girth', 'Height']]  # x는 Girth와 Height 열을 포함하는 데이터프레임
# y = tree['Volume']  # y는 Volume 열을 포함하는 시리즈
#
# model = keras.Sequential()
# model.add(keras.layers.Dense(1))
#
# model.compile(optimizer=keras.optimizers.SGD(0.0001),
#               loss=keras.losses.mse)
#
# model.fit(x, y, epochs=10, verbose=1)
#
# # Girth가 15이고 Height가 80일 때의 Volume 예측
# new_data = pd.DataFrame({'Girth': [15], 'Height': [80]})
# predicted_volume = model.predict(new_data)
# print("Predicted Volume:", predicted_volume[0][0])


# 강사님 코드
def read_trees():
    trees = pd.read_csv('data/trees.csv', index_col=0)
    print(trees)

    return trees.values[:, :-1], trees.values[:, -1:]

x, y = read_trees()
read_trees(x.shpae, y.shpae)

model = keras.Sequential()
model.add(keras.layers.Dense(1))

model.compile(optimizer=keras.optimizers.SGD(0.0001),
              loss=keras.losses.mse)

model.fit(x, y, epochs=10, verbose=2)

print(model.predict([[10, 70],
                     [15, 80]]))