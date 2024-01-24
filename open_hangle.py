# http://openhangul.com/nlp_ko2en?q=%ED%95%9C%EA%B8%80

# 오픈 한글 사이트에서 한글 자판을 알파벳 자판으로 바꿔주는 서비스를 사용해서
# 특정 단어를 변환하는 코드를 만드세요
import re
import requests
import json

def convert(hangul):
    url = 'http://openhangul.com/nlp_ko2en?q=' + hangul
    response = requests.get(url)
    # print(response)
    # print(response.text)
    # print(response.content)         # 일반적으로 HTTP 요청 후 서버로부터 받은 응답의 내용

    print("-" * 50)
    text = response.content.decode('utf-8')
    # print(text)
    # <img src="images/cursor.gif">

    codes = re.findall(r'<img src="images/cursor.gif"><br>([a-z]+)',text)
    # codes = re.findall(r'<img src="images/cursor.gif"><br>(.+)',text)         #.+ : 아무 문자나 찾아라
    # print(codes)
    return codes[0]

# 입력한 단어에 대해서 함수로 만든다
print(convert('하늘'))
print(convert('점심'))
print(convert('아이돌'))
print(convert('파이썬'))
print(convert('컴퓨터'))
