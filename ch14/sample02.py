from io import StringIO
import pandas as pd
import requests

user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
}

all_tabel_data = pd.DataFrame()
total_page = 5 # 737 많아서 5개만

# 1 - 737 페이지 크롤링
for page in range(1, total_page + 1):
    print('-' * 50)
    print(f'{page} / {total_page}')

    url = f'https://finance.naver.com/item/sise_day.naver?code=005930&page={page}'
    response = requests.get(url, headers = user_agent)

    print(response.status_code)
    # print(response.headers)
    # print(response.text)

    raw_html = response.text
    raw_data = pd.read_html(StringIO(raw_html))

    # print(type(raw_data))
    # print(len(raw_data))

    table_data = raw_data[0]
    # print(type(table_data))

    # print('-' * 40)
    # print(table_data.info())
    print('-' * 90)
    print(table_data.head())

    all_tabel_data = pd.concat([all_tabel_data, table_data])

all_tabel_data.dropna(inplace = True)

print(all_tabel_data.head())
all_tabel_data.to_csv('all_table_data.csv')