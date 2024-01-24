import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)

print('-'*50)


# 퀴즈
# 2차원 배열 마지막 요소를 출력해 보세요(11)

print(a[-1, -1]) # [시작, 종료] -> fancy indexing

print('-'*50)

# 퀴즈
# 마지막 열만 출력해 보세요
print(a[-1: :])         #  a[-1: :] 3행 부터 끝까지
print(a[:, -1])         # 1차원 출력

print('-'*50)


print(a[-1:, :])         #  : 을 붙이면 2차원 배열 출력
print(a[:, -1:])

print('-'*50)

print(np.zeros(3))      # 0 으로 채운다
print(np.zeros(3, dtype=np.int32))
print(np.zeros((3, 4)))
print(np.ones((3, 4)))
print(np.full((3, 4), fill_value=-1))   # 3행 4열 배열을 -1 로 채운다.

print('-'*50)

b = np.zeros((5, 5), dtype=np.int32)
print(b)

# 퀴즈
# 테두리를 1로 채워 보세요

b[0] = 1
b[-1] = 1
b[:, 0] = 1
b[:, -1] = 1

#퀴즈 위 코드를 인덱스 배열로 수정

b[[0, -1]] = 1
b[:, [0, -1]] = 1

print(b)

print('-'*50)

# 퀴즈
# 2차원 배열의 속을 2로 채워보세요
b[1:-1, 1:-1] = 2           # 1:-1 -> 행 에 대한 슬라이싱 인덱스 1부터 끝에서 두 번째 까지 선택

print(b)

print('-'*50)

# 퀴즈
# 2차원 배열의 대각선을 3으로 채워보세요

# 첫번 째 방법
# b[0, 0] = 3
# b[1, 1] = 3
b[[0, 1], [0, 1]] =3        #  인덱스 배열 -> 많이 사용, 첫 번째 [0, 1]: 행의 인덱스를 나타내며, 여기서는 0번째 행과 1번째 행을 선택
b[range(5), range(5)] = 3

#두번 째 방법
# for i in range(len(b)):
#     b[i, i] = 3

print(b)

print('-'*50)

c1 =np.arange(12).reshape(3, 4)
c2 =np.arange(12).reshape(4, 3)

print(np.dot(c1, c2))  # dot : 2차원 행렬 곱셉을 곱한다.

print(c1)
print(np.transpose(c1))  # 대각선 기준으로 회전한다.




















