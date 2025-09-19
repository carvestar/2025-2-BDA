'''
다음 소스 코드는 40명의 학생에게 50~100점 사이의 점수(50이상, 100이하)를 무작위로 할당한 딕셔너리 scores를 제공한다.
각 문제의 정답을 제시하기 위한 소스 코드를 작성하고 결과를 입력하시오.
'''

import random

scores = dict()
for i in range(10, 50):
    scores['S' + str(i)] = random.randrange(50, 100 + 1)
print(scores)

# 40명의 학생의 평균 점수를 구하시오.
sum_value = 0
'''
for value in scores.values():
    sum_value += value
print(sum_value)
'''

sum_value = sum(scores.values())
cnt = len(scores)
avg = sum(scores.values()) / len(scores)
print(avg)