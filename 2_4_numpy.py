# numhpy
import numpy as np

a = list('abcdefg')
print(a)

print(a[0], a[-1])
print(a[:3])  # 3번 쨰 까지 출력
print(a[3:])    # 3번 째 부터 출력
print(a[::2])   # 증감
print('-' *30)

b = np.arange(12)   # arange(12) : 0 ~ 12 하나씩 증가
# b = np.arange(0, 12)   # arange(12) : 0 ~ 12 하나씩 증가
# b = np.arange(0, 12, 1)   # arange(12) : 0 ~ 12 하나씩 증가
print(b)
print(type(b))          # <class 'numpy.ndarray'>
print(b.shape, b.dtype, b.size)
print('-' *30)

print(b + 1)    # broadcast, 배열의 사이즈 상관없이 +1 한다. 중요
print(b * 1)
print(b > 5)    # 관계 연산자
print(3 * b)
print(b + b)    # vector   중요
print(np.sin(b))    # universal function 중요
print(sum(b))
print('-' *30)

c = b.reshape(3, 4)     # 2차원 배열 3행 4열
print(c)
print('-' *30)

print(c + 1)        # broadcast
print(c + c)        # vector
print(np.sin(c))    # universal  cos, tan 포함
print(np.cos(c))
print('-' *30)

d = b.reshape(3, 4)
# d = b.reshape(3, -1)
# d = b.reshape(-1, 4)
print(d)
print('-' *30)

#퀴즈
# 2차원 배열을 1차원으로 변환해라(3가지)
print(b.reshape(12))        # 맞았음
print(d.reshape(d.size))
print(d.reshape(len(d) * len(d[0])))
print(d.reshape(-1))  # 다 차원에서 1차원으로 변경할 때 사용

print('-' *30)

e = np.arange(4)
f = np.arange(12).reshape(3, 4)
print(e)
print(f)
print(e + f)