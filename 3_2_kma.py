
import re
import requests

url = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
response = requests.get(url)
# print(response)     # Response [200]
# print(response.text)
# print(response.content)
# <province>서울ㆍ인천ㆍ경기도</province>
text = response.content.decode('utf-8')

codes = re.findall(r'<province>(.+)</province>', response.text)
print(codes)
print('-' * 50)

# location을 찾는다.
# DOTALL 여러 줄에 걸쳐 있을 떄 사용(개행 문자를 무시)
# .+ : greedy(탐욕적)
# .+? : non-greedy(비탐욕적)
location = re.findall(r'<location wl_ver="3">(.+?)</location>+', response.text, re.DOTALL)   # (.+)안에 있는 내용은 전부 찾아라
print(len(location))

print(re.findall(r'<location (.+)>+', text))

print('-' * 50)

# province 를 찾아라
# <province>서울ㆍ인천ㆍ경기도</province>
province = re.findall(r'<province>서울ㆍ인천ㆍ경기도</province>+', response.text)
province2 = re.findall(r'<province>(.+?)</province>+', response.text, re.DOTALL)
print(province)
print(len(province))



for loc in location:            # loc : 문자열 검색
    # print(loc)
    prov = re.findall(r'<province>(.+)</province>+', loc)      # re.DOTALL 작성해도 provincs는 한 개 이기에 효과가 없다.
    city = re.findall(r'<city>(.+)</city>+', loc)      # re.DOTALL 작성해도 provincs는 한 개 이기에 효과가 없다.
    print(prov, city)
    break

print('-' * 50)

    # 퀴즈
    # provice 와 city를 한번에 찾아보세요
# for loc in location:
#
#     print(re.findall(r'<province>(.+)</province>+', loc) for loc in location)
#     break


for loc in location:
    result = re.findall(r'<province>(.+)</province>', loc)
    if result:
        print(result[0])
print('-' * 50)
# 강사님 코드
for loc in location:            # loc : 문자열 검색
    # print(loc)
    prov = re.findall(r'<province>(.+)</province>+', loc)      # re.DOTALL 작성해도 provincs는 한 개 이기에 효과가 없다.
    city = re.findall(r'<city>(.+)</city>+', loc)      # re.DOTALL 작성해도 provincs는 한 개 이기에 효과가 없다.
    # print(prov, city)

    pv = re.findall(r'<province>(.+)</province>.+<city>(.+)</city>', loc, re.DOTALL)        # .+ 을 이용해서 연결
    print(pv)
    break

print('-' * 50)

# data를 찾아라
# <data> </data>

data = re.findall(r'<data>(.+?)</data>+', loc, re.DOTALL)
print(len(data))
print(data)
print('-' * 50)

# data 안에 포함된 mode, tmEf, wf, tmn, rnSt를 찾아보세요

# <mode>A02</mode>
# <tmEf>2024-01-15 00:00</tmEf>
# <wf>맑음</wf>
# <tmn>-7</tmn>
# <tmx>1</tmx>
# <reliability/>
# <rnSt>10</rnSt>

for loc in location:            # loc : 문자열을 찾아라
    all = re.findall(r'<mode>(.+?)</mode>.+<tmEf>(.+?)</tmEf>.+<wf>(.+?)</wf>.+<tmn>(.+?)</tmn>.+<tmx>(.+?)</tmx>.+<rnSt>(.+?)</rnSt>', loc, re.DOTALL)
    print(all)
    break

print('-' * 50)

#강사님

# csv_file_path = 'kma.csv'
# with open(csv_file_path, 'w', newline='', encoding='utf-8') as f:
#     # CSV 파일 헤더 작성
#     f.write('Province, City, Mode, tmEf, wf, tmn, tmx, rnSt\n')
# for datum in data:
#     mode = re.findall(r'<mode>(.+)</mode>', datum)
#     tmEf = re.findall(r'<tmEf>(.+)</tmEf>', datum)
#     wf = re.findall(r'<wf>(.+)</wf>', datum)
#     tmn = re.findall(r'<tmn>(.+)</tmn>', datum)
#     tmx = re.findall(r'<tmx>(.+)</tmx>', datum)
#     rnSt = re.findall(r'<rnSt>(.+)</rnSt>', datum)
#     print(prov[], city[], mode[], tmEf[], wf[], tmn[], tmx[], rnSt[])
#     f.write('{}, {}, {}, {}, {}, {}, {}, {}\n'.format(prov[0], city[0], mode[0], tmEf[0], wf[0], tmn[0], tmx[0], rnSt[0]))
#
# print(f'CSV 파일이 생성되었습니다: {csv_file_path}')

csv_file_path = 'kma.csv'

# 파일을 열고 쓰기 모드로 유지하기 위해 with 문을 사용합니다.
with open(csv_file_path, 'w', newline='', encoding='utf-8') as f:
    # Create CSV file header
    f.write('Province, City, Mode, tmEf, wf, tmn, tmx, rnSt\n')

    for datum in data:
        mode = re.findall(r'<mode>(.+)</mode>', datum)
        tmEf = re.findall(r'<tmEf>(.+)</tmEf>', datum)
        wf = re.findall(r'<wf>(.+)</wf>', datum)
        tmn = re.findall(r'<tmn>(.+)</tmn>', datum)
        tmx = re.findall(r'<tmx>(.+)</tmx>', datum)
        rnSt = re.findall(r'<rnSt>(.+)</rnSt>', datum)

        # Print each value
        print(prov[0], city[0], mode[0], tmEf[0], wf[0], tmn[0], tmx[0], rnSt[0])

        # CSV 파일에 쓰기
        f.write('{}, {}, {}, {}, {}, {}, {}, {}\n'.format(prov[0], city[0], mode[0], tmEf[0], wf[0], tmn[0], tmx[0], rnSt[0]))

print(f'CSV 파일이 생성되었습니다: {csv_file_path}')


f.close()
    # items = re.findall(r'<[A-Za-z]+>(.+)<[A-Za-z]+>', datum)
    # items = re.findall(r'<\w+>(.+)<\w>', datum)
    # items = re.findall(r'>(.+)<', datum)
    # hprint(items)

    # print(items)

# 퀴즈
# 앞에서 출력한 내용으로 kma.csv 파일을 만드세요
# csv_data = []

# for loc in location:
