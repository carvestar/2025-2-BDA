my_Book = (2002, '파이썬', 200, '1교시')
your_Book = [2002, '파이썬', 200, '1교시']
#            0      1       2    3

# other_Book = your_Book
# other_Book = [your_Book[0], your_Book[1], your_Book[2], your_Book[3]]로 하면 your_Book과 다른 주소값
other_Book = your_Book[0:4]     # 슬라이싱 이용하면 새롭게 메모리 만들어짐, [0:4] == [:]


print(my_Book)
print(your_Book)
print(other_Book)

print(id(my_Book))
print(id(your_Book))
print(id(other_Book))       # your_Book과 주소값 같음

other_Book[0] = 2025        # other_Book 바꾸면 your_Book도 바뀜
print(my_Book)
print(your_Book)
print(other_Book)

new_Book = your_Book[1:2 + 1]       # == [1:3]
print(new_Book)

new_Book2 = my_Book[1:3]
print(new_Book2)