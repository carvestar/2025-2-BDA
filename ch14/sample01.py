# pip install lxml
from io import StringIO
import pandas as pd
import requests

user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
}
url = 'https://www.dongyang.ac.kr/dmu/4904/subview.do'

'''
# .do, .php, .asp(.aspx), .jsp, .naver, 확장자(x)
# 주소: 물리적 주소(특정 파일로 존재) vs 논리적 주소(매칭은 되지만 파일로 존재하진 않음)
# protocol -> https
# host(domain) -> www.dongyang.ac.kr
# page name -> /dmu/4904/subview.do
# querystring -> .do?...(뒷내용)
# url(uri)
# 데이터 요청 5가지 메소드: get, post(숨겨야 하는 데이터 비밀번호와 같은), delete(데이터 삭제), put(데이터 수정), fetch(일부 데이터 수정)
# fiddler

# http -> 프로토콜
# http(80), https(443), ftp(20, 21), smtp(25)
# 네트워크상 5개: ip(필수), port(필수), instance, account, password
# 동양미래대학교 웹서비스 IP: 203.249.39.43, port: 80(http)
# http://203.249.39.43:80
# https://203.249.39.43:443 -> 주의
# www.dongyang.ac.kr (도메인 서비스) : 도메인 네임 서버
'''

response = requests.get(url, headers = user_agent)

print(response.status_code)
# print(response.headers)
# print(response.text)

raw_html = response.text
raw_data = pd.read_html(StringIO(raw_html))

print(type(raw_data))
print(len(raw_data))

table_data = raw_data[0]
print(type(table_data))

print('-' * 40)
print(table_data.info())
print('-' * 90)
print(table_data.head())