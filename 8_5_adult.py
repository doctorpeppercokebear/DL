import pandas as pd
import numpy as np
import tensorflow.keras as keras
from sklearn import model_selection, preprocessing


def read_adult():
    adult = pd.read_csv('data/adult.data', header=None)

    x = [adult[0].values,
         adult[2].values,
         adult[4].values,
         adult[10].values,
         adult[11].values,
         adult[12].values,
         ]

    x = np.float32(x).transpose()

    bin = preprocessing.LabelBinarizer()
    y = bin.fit_transform(adult[14])
    print(y)

    work = bin.fit_transform(adult[1])
    edu = bin.fit_transform(adult[3])
    marital = bin.fit_transform(adult[5])
    occu = bin.fit_transform(adult[6])
    rel = bin.fit_transform(adult[7])
    race = bin.fit_transform(adult[8])
    sex = bin.fit_transform(adult[9])
    country = bin.fit_transform(adult[13])
    print(work)
    print(work.shape)

    x = np.hstack([x, work, edu, marital, occu, rel, race, sex, country])
    print(x.shape)
    return x, y


x, y = read_adult()

data = model_selection.train_test_split(x, y, train_size=0.7)
x_train, x_test, y_train, y_test = data

model = keras.Sequential()
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.binary_crossentropy,
              metrics='acc')

model.fit(x_train, y_train, epochs=10, verbose=2,
          validation_data=(x_test, y_test))
