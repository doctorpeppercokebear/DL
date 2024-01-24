import numpy as np



def  softmax_1(z):
    return z / np.sum(z)


z = [2.0, 1.0, 0.1]

print(softmax_1(z))

# 퀴즈
# softmax 를 함수로 만들어 보세요

def softmax_2(z):
    z = np.e ** np.array(z)     # np.e 상수라서 오류
    return z / np.sum(z)