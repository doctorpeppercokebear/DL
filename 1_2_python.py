# 함수

def f_1(a, b, c):
    print(a, b, c)

f_1(1, 2, 3)         # positional
f_1(a=1, b=2, c=3)   # keyword -> 숫서는 상관 없다.
f_1(b=2, a=1, c=3)   # keyword
f_1(1, 2, c=3)   # positional, keyword 섞음 대신 keyword는 마지막에 작성

# f_2를 5가지 방식으로 호출
def f_2(a=0, b=0,c=0):
    print(a, b, c)

f_2()
f_2(1, 2, 3)
f_2(1,2)
f_2(1)
f_2(c=1)
f_2(a=1, c=3)

print('-' * 10)
# sep : 문자열 사이 출력 , *args



#  퀴즈
# 0 ~ 100 사이의 ㄴ난수 10개로 이루어진 리스트를 만드세요

import random
numbers = [0, 10]
number = random.randrange(100)
print(number)

random.seed(41)
print(random.randrange(100))

a = []
for _ in range(10):         # _ 사용 안하는 건 밑줄 처리
    a.append(random.randrange(100))
print(a)

# 리스트를 만드는 한 줄 짜리 반복문 리스트 컴프리레이션
b = []
for _ in range(10):         # _ 사용 안하는 건 밑줄 처리
    b.append(random.randrange(100))

print(b)

print('-' * 10)

b = [random.randrange(100) for _ in range(10)]   # 리스트 컴프리레이션ㅣ
print(b)

print("-" * 50)

print("Mob Psycho 100", end="")

print("Mob Psycho 100")

print('-' * 50)

# 리스트 b를 거꾸로 출력해라

b = [random.randrange(100) for _ in range(10)]   #
print(b)

# 방법 1
b.reverse()
print(b)

# 방법 2
b = [random.randrange(100) for _ in range(10)]
print(b)

reverse_b = b[:: -1] # :: 첫번 째 인덱스 부터 마지막 인덱스 까지 출력, -1 : 스텝을 나타내며 역순으로 추출
print(reverse_b)

print('-' * 50)

# 강사님 코드
print(*b[::-1])   # 리스트를 벗겨낸다.

for i in range(len(b)-1, -1, -1):
    print(b[i], end=' ')
print()

for i in reversed(range(len(b))):
    print(b[i], end=' ')
print()

for i in reversed(b):
    print(i, end='')
print()

b.reverse()
print(*b)

print('-' * 50)
# 다중 치환
n = 3
m = 9
print(n)

print(m, n)

n, m = 3, 8
print(n, m)

n, m = m, n
print(n, m)

k = m, n    # 오른 쪽 개수가 더 많으면 튜플로 처리
print(k)
print(k, k[0], k[1])

t = 1, 3, 5
print(*t, sep='')    # sep : 여러개 값이 넘어갈 때 사이사이 출력, * : 쉼표 없이 붙여서 출력
print(t, sep='')

# 퀴즈
# 리스트 b 에서 홀수만 출력

b = [random.randrange(100) for _ in range(10)]

b = [num for num in b if num % 2 != 0]   # !=  -> 같지 않다.

print(b)

for i in b:
    if i % 2:
        print(i)

print([i for i in b if i % 2])

print('-' * 50)

def to_lower(s):
    return s.lower()

color = ['red','green','YELLOW','blue']
print(sorted(color))
print(sorted(color, key=to_lower))
print(sorted(color, key=to_lower, reverse=True))

## 퀴즈
# color를 글자 갯수순으로 정렬하세요  -> len()을 통해서 글자 수 파악 후 정렬하면 될 거 같다.

def str_len(s):
    return len(s)

print(sorted(color, key=str_len))
print(sorted(color, key=lambda s: len(s)))
print(sorted(color, key=len))

print('-' * 50)
### 퀴즈
# 10000 보다 작은 양수에 포함된 8의 갯수는?
# 리스트에 10000 보다 작은 수 and 8이 포함된 숫자를 넣어야함 그리고 리스에 있는 숫자에 8의 갯수를 개수를 구하고 더한다.

for i in range(10000):
    if i > 10000 and i in 8:
        print()


s = 0
for i in range(1, 10001):
    s += str(i).count("8")
print(s)

# print(s for i in range(1, 10001) for)

# for i in range(90, 100):
#     for c in str(i):
#         if c == '8':
#             print(c)

print('-' * 50)

print(len([c for i in range(10000) for c in str(i) if c == '8']))

print('-' * 50)



print('808'.count('8'))
print([str(i) for i in range(10)])
print([str(i).count('8') for i in range(10000)])

print(sum(str(i).count('8') for i in range(10000)))
print(str(list(range(10000))).count('8'))
