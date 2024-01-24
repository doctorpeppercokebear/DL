import re

import requests
import json
url = 'https://www.naver.com/'
url = 'https://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
response = requests.get(url)
print(response)
print(response.text)
print(response.content)

text = response.content.decode('utf-8')     #decode :
print(text)

print('-' * 50)
# [{"code":"11","value":"서울특별시"},{"code":"26","value":"부산광역시"},{"code":"27","value":"대구광역시"},{"code":"28","value":"인천광역시"},{"code":"29","value":"광주광역시"},{"code":"30","value":"대전광역시"},{"code":"31","value":"울산광역시"},{"code":"41","value":"경기도"},{"code":"42","value":"강원도"},{"code":"43","value":"충청북도"},{"code":"44","value":"충청남도"},{"code":"45","value":"전라북도"},{"code":"46","value":"전라남도"},{"code":"47","value":"경상북도"},{"code":"48","value":"경상남도"},{"code":"50","value":"제주특별자치도"}]

# 퀴즈
# 기상청에서 읽어온 데이터 로부터 code와 value 만 출력하세요
# 예시 ) 11 서울시  26 부산광역시


db = '''  
[{"code": "11", "value": "서울특별시"}, {"code": "26", "value": "부산광역시"}, {"code": "27", "value": "대구광역시"},
 {"code": "28", "value": "인천광역시"}, {"code": "29", "value": "광주광역시"}, {"code": "30", "value": "대전광역시"},
 {"code": "31", "value": "울산광역시"}, {"code": "41", "value": "경기도"}, {"code": "42", "value": "강원도"},
 {"code": "43", "value": "충청북도"}, {"code": "44", "value": "충청남도"}, {"code": "45", "value": "전라북도"},
 {"code": "46", "value": "전라남도"}, {"code": "47", "value": "경상북도"}, {"code": "48", "value": "경상남도"},
 {"code": "50", "value": "제주특별자치도"}
]'''

# json_data = json.loads(('[' + db + ']'))
#
# code_list = [entry['code'] for entry in json_data]
# valuelist = [entry['value'] for entry in json_data]
#
# print([code_list, valuelist])

# for k in db:
#     print(k, db[k])

# print(db.key())
# print(db.values())

items = json.loads(text)
# print(type(items))
for item in items:
    # print(item, type(item))
    # for k in item:
    #     print(item[k], end='')
    # print()

    print(item['code'], item['value'])

print('-' * 50)

# 퀴즈
# 기상청에서 읽어온 데이터 로부터 code와 value 만 출력하세요  문자열로

for i in db:
    pass


print(re.findall(r'[0-9]+', db))
print(re.findall(r'[ㄱ-ㅣ가-힣]+', db))

print('-' * 50)

codes = re.findall(r'[0-9]+', text)
values = re.findall(r'[가-힣]+', text)
print(codes)
print(values)

print('-' * 50)
codes1 = re.findall(r'"code":"[0-9]+"', text)      # () : 원하는 값만 가져온다
values1 = re.findall(r'"value":"[가-힣]+"', text)

for i in range(len(codes1)):
    print(codes1[i], values1[i])

print('-' * 50)

for c,v in zip(codes, values):          # zip : 값을 묶어주는 역할 -> 양쪽의 개수가 같을 때 사용한다
    print(c, v)

print('-' * 50)
# findall 함수를 한 번만 사용해서 결과 출력
cv = re.findall(r'{"code": "([0-9]+)", "value": "([가-힝]+)"}', db)
for a, b in cv:
    print(a, b)