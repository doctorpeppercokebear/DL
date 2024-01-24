import re
import json


## 1.  hello 를 3번 출력하는 코드를 5개 만드세요

print('hello', 'hello', 'hello')

for i in range(3):
    print("hello")

print('hello hello hello')

print('-' * 100)

# f_2 를 5가지 방식 으로 호출해 보세요

# 0~100 사이의 난수 10개로 이루어진 리스트를 만드세요
import random
b = [random.randrange(100) for _ in range(10)]
print(b)

print('-' * 100)

# 리스트 b를 거꾸로 출력하세요
print(b[::-1])

print(b.reverse())


print('-' * 100)

# 리스트 b 에서 홀수만 출력하세요
for i in b:
    # if i % 2 == 1 :
    if i % 2:      # 이미 0은 참 1은 거짓으로 정의 되어있다.
        print(i)

print(i % 2 for i in range(len(b)))
print('-' * 100)

# n과 m의 값을 바꾸세요
n, m = 4, 5
n, m = m, n
print(n, m)
print('-' * 100)

# colors를 대소문자 무시한 순서로 정렬하세요
colors = ['red','grenn','YELLOW','blue',]

# 10000 보다 작은 양수에 포함된 8의 개수는?

# poem.txt 파일에 들어있는 단어 갯수를 구하라

# 24/01/11

db = ''' 3412    [Bob] 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534
'''

# 숫자만 찾아보세요
print(re.findall(r'[0-9]+'), db)
# 이름만 찾아보세요

# T 로 시작하는 이름만 찾아보세요
print(re.findall(r'T[A-Za-z]+', db))
# exit()
print(re.findall(r'T[a-z]+', db))


# T로 시작하지 않는 이름만 찾아보세요
print(re.findall(r'[^T][A-Za-z]+', db))
print(re.findall(r'[A-SU-Z][a-z]+', db))    # a-z 까지 순서대로 출력인데 중간에 s t u 순인데 t를 제외해야 하니까 A-SU-Z가 나온다.


# url = 'https://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
#  response = requests.get(url)

# 기상청에서 읽어온 데이터로부터 code와 value만 출력(json)
# 기상청에서 읽어온 데이터로부터 code와 value만 출력(정규 표현식)
