# 1_4_attendant.py

# 퀴즈
# 행사 참석자에 대해 엑셀 파일로 깔끔하게 만드세요
members = '''김정훈/참석/숙박/A
김희자/참석/숙박/A
정운석/참석/숙박/B
손상연/참석/숙박/B
송은숙/참석/숙박/B
이상기/참석/숙박/B
안은하/참석/숙박/B
라경향/참석/숙박×/A
류제록/참석/숙박/B
최보금/참석/숙박/B
정연호/참석/숙박/A
김태임/참석/숙박/A
손종남/참석/숙박/A
강경삼/참석/숙박/A
이승준/참석/숙박/C
이준섭/참석/숙박/A
권민주/참석/숙박/A
임희재/참석/숙박/A
이충환/참섴/숙박/A
김순태/참석/숙박/A
박용우/참석/숙박/A
박웅현/참석/숙박×/A
김영석/참석/숙박/A
이승창/참석/숙박/A
하이순/참석/숙박/X
박영경/참석/숙박/B
김숙희/참석/숙박/A
신동원/참석/숙박/A
최병국/참석/숙박x/C
최귀순/참석/숙박/B
김태은/참석/숙박/B
전은순/참석/숙박/B
임정연/참석/숙박/B
윤재문/참석/숙박/A
김완기/참석/숙박/C
김윤정/참석/숙박/A'''

f = open('data/attendant.csv', 'w', encoding='euc-kr')

print('이름,참석,숙박,급수', file=f)
for row in members.split('\n'):
    name, _, sleep, level = row.split('/')
    print(name, 'O', 'O' if sleep == '숙박' else 'X', level,
          sep=',', file=f)

f.close()
