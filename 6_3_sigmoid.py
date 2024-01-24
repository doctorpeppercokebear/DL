#6_3 sigmoid.py
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.e ** -z)

print(np.e)     # e : 오일러 상수

for z in np.linspace(-10, 10):
    s = sigmoid(z)
    print('{:.5} : {:.5}'.format(z, s))

    plt.plot(z, s, 'ro')

    plt.plot(z, s, 'ro')
plt.show()

def cross_entropy(y):
    def log_a():
        return 'a'
    def log_b():
        return 'b'

    print(y * log_a() + (1-y) * log_b())


# show_sigmoid
cross_entropy(y=0)
cross_entropy(y=1)

