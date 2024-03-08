'''
flower18
    - train
        -buttercup
        -coltsfoot
        -daffodil
    - test
        -buttercup
        -colsfoot
'''
import keras.preprocessing.image
import numpy as np
import matplotlib.pyplot as plt

# 이미지 데이터를 증강하고 전처리 하는데 사용하는 클래스
# 이미지 데이터의 그키, 회전, 밝기 등을 변형하여 모델의 학습 데이터를 늘리고 일반화 성능을 향상 시키는데 도움
gen = keras.preprocessing.image.ImageDataGenerator(
    rescale=1/255,
    # zoom_range=5,
    width_shift_range=50,

)


# 180 images belonging to 3 classes
flow = gen.flow_from_directory('flower17/train',
                               target_size=(224, 224),
                               class_mode='sparse',
                               batch_size=4,
                               shuffle=False
                               )

for x, y in flow:
    # print(x.shape, y.shape)
    # print(y)

    plt.imshow(x[0] / 255)

# print(flow.classes)
# print(flow.labels)
# print(flow.class_indices)       # {'buttercup': 0, 'coltsfoot': 1, 'daffodil': 2}



