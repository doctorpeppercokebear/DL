# 4_4_pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 5, 7])  # 1차원 데이터 시리즈 결과값 왼쪽 인덱스 오른쪽 values
print(s)

print(s.index)
print(s.values)

print('*' * 50)


print(s[0])
print(s[3])

print('*' * 50)

s.index = ['a', 'b', 'c', 'd']
print(s['a'])
print(s['d'])

print('*' * 50)

data = {
    'city': ['mokpo', 'mokpo', 'mokpo', 'busan', 'busan', 'busan'],
    'year': [2021, 2022, 2023, 2021, 2022, 2023],
    'population': [300, 400, 350, 250, 300, 350 ]
}

df = pd.DataFrame(data)
print(df)

print('*' * 50)

print(df.index)
print(df.columns)
print(df.values)

df.index = list('abcdef')

print(df['city'])
print(df.iloc[0])       # 행 데이더 접근  순서로 접근 iloc, 시리즈로 출력
print(df.loc['a'])       # 행 데이더 접근 인덱스로 접근 loc,

print(df.iloc[:3])

print('*' * 50)


# 퀴즈
# 인덱스 키를 사용해서 부산 데이터만 출력하세요

#  자주 사용하지 않는다.
print(df.loc['d':])   # 'd' 부터 끝까지
print(df.loc['d':'f'])   # 'd' 부터 'f' 까지
