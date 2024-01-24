# 퀴즈
# 한국음악저작권협회에서 지드랜곤의 저작권 데이터를 가져오세요

import re
import requests

payload = {
    'S_PAGENUMBER': '5',
    'S_MB_CD': 'W0726200',
    'S_HNAB_GBN': 'I',
    'hanmb_nm': 'G-DRAGON',
    'sort_field': 'SORT_PBCTN_DAY',
}
url = 'https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
response = requests.post(url, data=payload)
# print(response)     # Response [200]
# print(response.text)
# print(response.content)

#  <th scope="col">저작물명</th>
# <td> 봄여름가을겨울(STILL LIFE)</td>

# codes = re.findall(r'<td>(.+?)</td>+', response.text)
tbody = re.findall(r'<tbody>(.+?)</tbody>+', response.text, re.DOTALL)
print(len(tbody))
print(tbody[1])

print('-' * 50)


# location = re.findall(r'<location wl_ver="3">(.+?)</location>+', response.text, re.DOTALL)   # (.+)안에 있는 내용은 전부 찾아라
# print(len(location))

# for loc in location:            # loc : 문자열 검색
#     # print(loc)
#     prov = re.findall(r'<province>(.+)</province>+', loc)      # re.DOTALL 작성해도 provincs는 한 개 이기에 효과가 없다.
#     city = re.findall(r'<city>(.+)</city>+', loc)      # re.DOTALL 작성해도 provincs는 한 개 이기에 효과가 없다.
#     print(prov, city)
#     break

#
# for loc in tbody:
#     title = re.findall(r'<th scope="col">저작물명</th>', loc, re.DOTALL)
#     singer = re.findall(r'<tr>(.+)</tr>+', loc, re.DOTALL)

trs = re.findall(r'<tr>(.+?)<tr>', tbody[1], re.DOTALL)
print(len(trs))

for tr in trs:
    # print(trs)
    tr = tr.replace('<br/>', ',')
    # tr = tr.replace(' <img src="/images/common/control.gif" alt="" />', '')
    # tr = tr.replace(' <img src="/images/common/control.gif"  alt="" />', '')   # 공백이 들어 가 있어서 둘 다 제거
    tr = re.sub(r'<img .+? />', '', tr)

    tds = re.findall(r'<td>(.*?)</td>', tr)  #(.+?): 아무 글자나 한 글자 찾아라, (.*?): 글자가 비워 있어도 찾는다
    tds[0] = tds[0].strip()
    print(tds)

# 퀴즈
# 앞에서 만드 코드를 함수로 바꾸고
# 지드래곤의 모든 노래를 가져와 보세요

def get_songs(code, page):
    payload = {
        'S_PAGENUMBER': page,
        'S_MB_CD': code,
        # 'S_HNAB_GBN': 'I',
        # 'hanmb_nm': 'G-DRAGON',
        # 'sort_field': 'SORT_PBCTN_DAY',
    }



get_songs(code='W0726200', page=1000)
