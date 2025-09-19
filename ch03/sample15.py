import copy

list_value = ['1', '2', '3', '4', '5', '6', '7', '8']
new_list_value = list_value[:]

print(list_value)
print(new_list_value)

list_value[0] = '11'

print('-' * 30)
print(list_value)
print(new_list_value)

print('-' * 30)
list_value = [['1', '2'], ['3', '4'], ['5', '6'], ['7', '8']]
print(len(list_value))

# new_list_value = list_value[:] 얕은 복사
new_list_value = copy.deepcopy(list_value)      # 깊은 복사: copy.deepcopy()

print(list_value)
print(new_list_value)

list_value[0][0] = '11'

print('-' * 30)
print(list_value)
print(new_list_value)

del new_list_value      # 깊은 복사 시 메모리 줄이기 위해 삭제