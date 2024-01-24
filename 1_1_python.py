# 1_1_python.py

# ctrl shift f10 -> 파일 실행
# alt + 1, + 4
# 퀴즈 hello 3번 출력하는 코드를 5개 만드세요
print('chat')
print('chat')
print('chat')
print('chat')
print('chat')
print('chaptgpt')  # ctrl c v (v를 원하는 만큼 누르면 복사됨)
print('chaptgpt')
print('chaptgpt')
print('chaptgpt')  # ctrl x 현재 줄 삭제

print('chaptgpt')  # shift 방향키
print('chaptgpt')
print('chaptgpt')
print('chaptgpt')  # ctrl / 주석 처리


# 1 번
str = 'hello'
print(str * 3)

# 2 번
for i in range(3) :
    print("hello")

# 3 번 리스트를 만들어서 3번 출력
# aa = []
# aa.append("hellow")
# aa.append("hellow")
# aa.append("hellow")

# class 만들어서
# class str2() :

## 강사님 코드
#1
print('hello hello hello')
#2
print('hello', 'hello', 'hello' )
# 3
print('hello')
print('hello')
print('hello')
# 4
print('hello'*3)
# 5
print('hello', 'hello', sep='hello')

# *    * (0, 4)
#  *  *  (1, 3)
#    *   (2, 2)
#  *  *  (3, 1)
# *    * (4, 0)
#  출력하기  규칙 행 과 열이 같다.


for i in range(5):
    for j in range(5):
        if i == j or i + j == 4:
            print("*", end='')
        else:
            print("-", end='')
    print()
print()

# *****  (0, 5, 1)
# *   *  (0, 5)
# *   *  (0, 5)
# *   *  (0, 5)
# *****  (0, 5, 1)
# 출력  0, 4 는 출력

for i in range(5):
    for k in range(5):
        # if i % 4 == 0 or k % 4 == 0:
        if i == 0 or i == 4 or k == 0 or k == 4:
            print("*", end='')
        else:
            print("-", end='')
    print()
print()




