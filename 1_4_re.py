# 정규 표현식
import re
# 개행 문자 포함
db = ''' 3412    [Bob] 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534
'''

# print(db)

print(re.findall(r'[0-9]+', db)) # r '' : 패턴 , 문자열

# . [] [^] ?  * + -> 정규 표현식 반드시 암기할 것

# 퀴즈
#이름만 찾아라

# 소문자가 더 크기에 앞에 나와야 한다
print(re.findall(r'[A-z]', db)) # bug

print(re.findall(r'[A-Za-z]+', db)) #just  대소문자 여러개 나와도 된다

print(re.findall(r'[A-Z][a-z]+', db)) #good  [A-Z]는 첫 번쨰 문자가 대문자 일때만 적용 가능한 규칙

print('-' * 100)
# 퀴즈
## T로 시작하는 이름만 찾아보세요
## T로 시작하지 않는 이름만 찾아보세요

print(re.findall(r'T[a-z]+', db))

print(re.findall(r'[^T][a-z]+', db))    # 틀렸어

print(re.findall(r'[ABCDEFGHIJKLMNOPQRSUVWXYZ][a-z]+', db))    # 틀렸어
print(re.findall(r'[A-SU-Z][a-z]+', db))    #








