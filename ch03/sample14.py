your_Book = [2002, '파이썬', 200, '1교시']
#            0      1       2    3

new_Book = your_Book

print('-' * 30)
print(your_Book)
print(new_Book)

your_Book[0] = 2025     # 깊은 복사

print('-' * 30)
print(your_Book)
print(new_Book)

new_Book = your_Book[:]     # 얕은 복사(슬라이싱)

print('-' * 30)
print(your_Book)
print(new_Book)

your_Book[0] = 2026

print('-' * 30)
print(your_Book)
print(new_Book)