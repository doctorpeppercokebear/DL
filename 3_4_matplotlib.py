import matplotlib.pyplot as plt
import numpy as np

def p1():
    plt.plot([1, 2, 3, 4], [1, 2, 3, 4], 'r')
    plt.plot([1, 2, 3, 4], [1, 2, 3, 4], 'gx')
    plt.show()

# y = x^2 그래프를 그려라
def p2():
    # x = range(-10, 10)
    # y = [i * i for i in x]
    # plt.plot(x, y)

    x = np.arange(-10, 10, 0.1)

    plt.plot(x, x**2)
    plt.show()

def p3():
    x = np.arange(0.1, 2, 0.1)

    plt.plot(x, np.log(x))
    plt.plot(x, -np.log(x))

    plt.plot(-x, np.log(x))
    plt.plot(-x, -np.log(x))

    plt.show




# p1()
# p2()
p3()