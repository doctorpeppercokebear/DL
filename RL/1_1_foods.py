'''
퀴즈
폴리텍 신기술 교육원의 식단 정보를 보여주세요
https://www.kopo.ac.kr/int/content.do?menu=2520
'''


import re
import numpy
import pandas
import keras
import matplotlib.pyplot as plt
import requests
import json



# def col():
#     url = 'https://www.kopo.ac.kr/int/content.do?menu=2520'
#     responce = requests.get(url)
#     # print(responce)
#     # print(responce.text)   # 한글 안 깨짐
#
#     # 코드 예시
#     codes = re.findall(r'<span>.+?</span>', responce.text)
#     date = re.findall(r'<td><script></script>(.+?)<br>월요일</td>', responce.text)
#
#     print(codes)
#     print(date)
# col()

'''
강사님 코드
'''
def solution1():
    url = 'https://www.kopo.ac.kr/int/content.do?menu=2520'
    response = requests.get(url)
    # print(response)
    # print(response.text)   # 한글 안 깨짐

    tbody = re.findall(r'<tbody>(.+?)</tbody>', response.text, re.DOTALL)
    # print(tbody)
    # print(len(tbody))

    tr = re.findall(r'<tr>(.+?)</tr>', tbody[0], re.DOTALL)
    # print(tr)

    for item, weekday in zip(tr, ('월', '화', '수', '목', '금', '토', '일')):
        item = item.replace('\r', '')
        span = re.findall(r'<span>(.*?)</span>', item)
        print('{}요일'.format(weekday))
        for meal, name in zip(span, ('아침', '점심', '저녁')):
            print(name, ':', meal)

    print('-' * 60)



'''
퀴즈
앞에서 만든 코드를 post 방식으로 수정하고
원하는 주(week)의 식단을 보여주세요
'''


def solution2(date):
    payload = {
        'day': date             #'20240219'
    }
    url = 'https://www.kopo.ac.kr/int/content.do?menu=2520'
    response = requests.post(url, payload)
    # print(responce)
    # print(responce.text)   # 한글 안 깨짐

    tbody = re.findall(r'<tbody>(.+?)</tbody>', response.text, re.DOTALL)
    # print(tbody)
    # print(len(tbody))

    tr = re.findall(r'<tr>(.+?)</tr>', tbody[0], re.DOTALL)
    # print(tr)

    for item, weekday in zip(tr, ('월', '화', '수', '목', '금', '토', '일')):
        item = item.replace('\r', '')
        span = re.findall(r'<span>(.*?)</span>', item)
        print('{}요일'.format(weekday))
        for meal, name in zip(span, ('아침', '점심', '저녁')):
            print(name, ':', meal)

def solution3():
    solution2('{}{:02}{:02}'.format())

solution1()
solution2(year=2024, month=3, day=5)