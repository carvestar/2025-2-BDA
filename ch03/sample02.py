my_Book = 2002, '파이썬', 200

print(type(my_Book))
print(my_Book)

print('-' * 20)
year, title, size = my_Book
print(year)
print(title)
print(size)

print('-' * 20)
print(my_Book[0])
print(my_Book[1])
print(my_Book[2])
# print(my_Book[3]) error!!

print('-' * 20)
print(my_Book[-1])
print(my_Book[-2])
print(my_Book[-3])
# print(my_Book[-4]) error!!

print('-'* 20)
print(len(my_Book))
print(my_Book[len(my_Book)-1])      # == print(my_Book[-1])