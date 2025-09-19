your_Book = [2002, '파이썬', '파이썬','파이썬',200]
print(your_Book)
print(type(your_Book))

# 기존 데이터 변경(리스트는 값 변경 가능)
your_Book[0] = 2025
print(your_Book)

# 데이터 맨뒤에 추가
your_Book.append('파이썬 프로그래밍')
print(your_Book)

# 데이터 원하는 위치에 추가
your_Book.insert(1, '프로그래밍 과목')
print(your_Book)

# 삭제(동일한 값 존재 시 하나만 삭제)
your_Book.remove('파이썬')
print(your_Book)

'''
존재하지 않는 값 삭제 시 에러
your_Book.remove('파이썬2')
print(your_Book)
'''

# 삭제 방법
if '파이썬2' in your_Book:
    your_Book.remove('파이썬2')
print(your_Book)