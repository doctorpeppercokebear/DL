'''
퀴즈
몬테 카를로 방법 으로 원주율 을 구하 세요
'''

import numpy as np
import matplotlib.pyplot as plt

inner, outer = [], []
cnt, n = 0, 1000000
for i in range(n):
    x = np.random.rand()
    y = np.random.rand()

    v = x ** 2 + y ** 2
    cnt += (v <= 1)

    if v<=1:
        inner.append((x,y))
    else:
        outer.append((x, y))

print(4 * cnt / n)        # 1 -4 분면이 있으니 4 를 곱한다.
plt.plot(*list(zip(*inner)), 'ro')
plt.plot(*list(zip(*outer)), 'bo')
plt.show()





































