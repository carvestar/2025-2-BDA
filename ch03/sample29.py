'''
다음 소스 코드는 40명의 학생에게 50~100점 사이의 점수(50이상, 100이하)를 무작위로 할당한 딕셔너리 scores를 제공한다.
각 문제의 정답을 제시하기 위한 소스 코드를 작성하고 결과를 입력하시오.

40명 중 최고 득점을 한 학생과 점수를 출력하시오.
여러 명인 경우, 학번이 가장 빠른 한 명만 출력되도록 하시오.
'''

import random

# 40명의 학생에게 50~100점 사이의 점수를 무작위로 할당
scores = dict()
for i in range(11, 50 + 1):
    scores['S' + str(i)] = random.randrange(50, 100 + 1)
print(scores)

# 최고 득점을 구하기
max_score = max(scores.values())

# 최고 득점한 학생 찾기 (여러 명일 경우 학번이 가장 빠른 학생을 출력)
top_student = None
for student, score in scores.items():
    if score == max_score:
        top_student = student
        break  # 학번 첫 번째인 학생을 선택

print(f"최고 득점은 {max_score}점이고, 최고 득점을 한 학생은 {top_student}입니다.")