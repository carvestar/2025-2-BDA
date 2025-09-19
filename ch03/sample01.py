my_Book = 2002, '파이썬', 200      # 튜플로 구성
my_Book2= (2002,'파이썬', 200)

print(type(my_Book))
print(my_Book)

print(type(my_Book2))
print(my_Book2)

year, title, size = my_Book     # 언패킹
print(year)
print(title)
print(size)