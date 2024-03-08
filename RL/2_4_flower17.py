import keras.preprocessing.image
import numpy as np
import matplotlib.pyplot as plt

# 이미지 데이터를 증강하고 전처리 하는데 사용하는 클래스
# 이미지 데이터의 그키, 회전, 밝기 등을 변형하여 모델의 학습 데이터를 늘리고 일반화 성능을 향상 시키는데 도움
gen_train = keras.preprocessing.image.ImageDataGenerator(rescale=1/255)

# 180 images belonging to 3 classes
flow_train = gen_train.flow_from_directory('flower17/train',
                               target_size=(224, 224),
                               class_mode='sparse',
                               batch_size=4,
                               shuffle=False
                               )

gen_test = keras.preprocessing.image.ImageDataGenerator(rescale=1/255)

# 180 images belonging to 3 classes
flow_test = gen_test.flow_from_directory('flower17/test',
                               target_size=(224, 224),
                               class_mode='sparse',
                               batch_size=4,
                               shuffle=False
                               )



# 2_3_vgg16.py
import keras

# model = keras.Sequential([
#     keras.layers.Input(shape=(224, 224, 3)),
#     keras.layers.Conv2D(8, 3, 1, 'same', activation='relu'),
#     keras.layers.MaxPool2D(2, 2),
#
#     keras.layers.Conv2D(16, 3, 1, 'same', activation='relu'),
#     keras.layers.MaxPool2D(2, 2),
#
#     keras.layers.Conv2D(32, 3, 1, 'same', activation='relu'),
#     keras.layers.MaxPool2D(2, 2),
#
#     keras.layers.Conv2D(64, 3, 1, 'same', activation='relu'),
#     keras.layers.MaxPool2D(2, 2),
#
#     keras.layers.Conv2D(64, 3, 1, 'same', activation='relu'),
#     keras.layers.MaxPool2D(2, 2),
#
#     keras.layers.Flatten(),
#
#     keras.layers.Dense(128, activation='relu'),
#     keras.layers.Dense(3, activation='softmax'),
# ])

conv_base = keras.applications.VGG16(include_top=False, input_shape=(224, 224, 3))
conv_base.trainable = False

model = keras.Sequential([
    conv_base,          # 미리 학습된 모델을 들고왔다.
    keras.layers.Flatten(),

    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(3, activation='softmax'),
])
model.summary()

model.compile(optimizer=keras.optimizers.RMSprop(0.001),
              loss=keras.losses.sparse_categorical_crossentropy,
              metrics='acc')
model.fit(flow_train, epochs=10, verbose=2,
          batch_size=100, validation_data=flow_test)