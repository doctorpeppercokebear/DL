import numpy as np
from sklearn import preprocessing

# 퀴즈
# cities 에 들어있는 문자열을 숫자로 변환세요

def encode(cities):
    print(set(cities))
    print(sorted(set(cities)))

    unique = sorted(sorted(cities))
    return [i for c in cities]

def label_encoder(cities):
    enc = preprocessing.LabelEncoder()
    enc.fit(cities)
    result = enc.transform(cities)
    print(result)
    print(enc.fit_transform(cities))

    print(enc.classes_)
    print(enc.inverse_transform(result))

    # 퀴즈
    # inverse_transform 코드를 만들어 보세요
    print(enc.classes_[result])

    print(np.identity(3))

print('-'*50)

# 퀴즈  240124 1523
# sparse 결과를 onehot 백터로 변환하세요
eye = np.identity(len(enc.classes_), dtype=np.int32)
print(eye[result])


def label_binarizer(cities):
    # 퀴즈
    # cities 문자열 리스트를 LabelBinarizer 클래스를 사용해서 숫자로 변환하세요
    bin = preprocessing.LabelBinarizer()
    bin.fit(cities)
    result = bin.transform(cities)
    print(result)
    print(bin.classes_)
    print(bin.inverse_transform(result))

    # 퀴즈
    # LabelBinarizer 객체가 만든 결과를 LabelEncoder가 만든 결과로 변환하세요
    print([list(i).index(1) for i in result])
    print([np.max(i) for i in result])
    print([np.argmax(i) for i in result])
    print(np.argmax(result))
    print(np.argmax(result, axis=1))


cities = ['bali', 'paris', 'london', 'bali', 'london']
# print(encode(cities))

label_encoder(cities)
# label_binarizer(cities)






















