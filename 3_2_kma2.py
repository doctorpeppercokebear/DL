import re
import requests

url = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
response = requests.get(url)
# print(response)     # Response [200]
# print(response.text)
# print(response.content)
# <province>서울ㆍ인천ㆍ경기도</province>



# 1. province 찾기
province = re.findall(r'<province>(.+)</province>', response.text)
# 2. location 찾기
# location = re.findall(r'<location wl_ver="3">(.?+)</location>+', response.txt)

# 3. provice 와 city를 한번에 찾아보세요

# 4. data를 찾아라

# 5. data 안에 포함된 mode, tmEf, wf, tmn, rnSt를 찾아보세요