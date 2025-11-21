import pandas as pd

file_name = '../ch11/data_raw.csv'
df_raw = pd.read_csv(file_name)

COL_LANG = 'LanguageHaveWorkedWith'

print('-' * 100)
print(df_raw.info())

ds_data = df_raw[COL_LANG]

# print('-' * 100)
# print(type(ds_data))                # Seriss

print('-' * 100)
print(ds_data)

print('-' * 100)

index = 0
lang_list = []
lang_set = set()

for c1 in ds_data:
    # print(index, c1, type(c1))      # str
    # split_data = c1.split(';')      # null을 실수형 데이터로 인식해 오류
    if type(c1) == str:             # split 전제 조건: str
        split_data = c1.split(';')
        for c2 in split_data:
            lang_list.append(c2)
            lang_set.add(c2)

print(lang_list)

JavaScript_count = 0

for c in lang_list:
    if c == 'JavaScript':
        JavaScript_count += 1

print('-' * 100)
print(JavaScript_count)

print('-' * 100)
print(lang_set)