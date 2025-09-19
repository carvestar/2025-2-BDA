data = { 'bgnde' : '2025.03.01',
         'sj' : '삼일절',
         'endde' : '2025.03.01'
}

'''
data_key_list = data.keys()
print(data_key_list)
print(type(data_key_list))      # 형태는 리스트지만 리스트는 아님
'''

for key in data.keys():
    print(key)

print('-' * 30)
for value in data.values():
    print(value)

print('-' * 30)
for item in data.items():
    print(item)
    print(item[0], item[1])
#    item[1] = 'abc'는 error! 튜플은 변형이 안 됨
print(type(item))

print('-' * 30)
for k, v in data.items():
    print(k, v)

# ctrl + alt + l = 정렬 단축