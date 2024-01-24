import matplotlib.pyplot as plt         # plot : 점을 찍거나 선을 연결

# cost function
def cost(x, y, w):
    c = 0
    for i in range(len(x)):
        hx = w * x[i]
        c += (hx - y[i]) ** 2

    return c / len(x)

def gradient_descent(x, y, w):          # 미분
    c = 0
    for i in range(len(x)):
        hx = w * x[i]
        c += (hx - y[i]) ** 2           # 미분
        # c += (w * y[i] - y[i]) ** 2  # 미분
        # c += 2 * (w * x[i] - y[i]) ** (2 - 1) * (w * x[i] - y[i])
        # c += 2 * (w * x[i] - y[i]) * x[i]

    return c / len(x)
def show_cost():
    # y = ax + b
    # hx = wx + b
    x = [1, 2, 3]
    y = [1, 2, 3]

     # 퀴즈
    # w, c 를 그래프로 그려보세요

    for i in range(-30, 50):
        w = i / 10
        c = cost(x, y, w)
        print(w, c)

        plt.plot (w, c, 'ro')
    plt.show()

def show_gradient():            # 학습이 안되고 있다. -> 발산
    x = [1, 2, 3]
    y = [1, 2, 3]

    #  퀴즈
    # w 를 1.0으로 만드는 코드 3가지를 찾아보세요.

    w = 5
    for i in range(5):
        c = cost(x, y, w)
        g = gradient_descent(x, y, w)       # g : 기울기
        w -= 0.2142 * g        # 학습률을 곱해서 발산을 막는다.
        # w -= g
        print(i, w)
#   기울기를 1로 변경하는 법
# 1. 학습률(w) 조정 --> 자동으로 조정, 2. 반복 횟수 조정

# 퀴즈
# x 가 5와 7일 때의 결과를 구하세요
    print('5:', w * 5)
    print('7:', w * 7)


show_gradient()

#

    # 미분 : 기울기, 순간변화량
    #        x축으로 1만큼 움직였을 때, y축으로 움직인 거리

    # y = 7         7 = 1, 7 = 2, 7 = 3  -> x 랑 y 랑 상관이 없다 : 미분 상수
    # y = x         1 = 1, 2 = 2, 3 = 3
    # y = (x + 1)   2 = 1, 3 = 2, 4 = 3
    # y = 2x        2 = 1, 4 = 2, 6 = 3

    #  y = x^2
    #  미분 : 2x


