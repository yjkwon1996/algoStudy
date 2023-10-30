# 일곱 난쟁이. 키의 합이 100이 되는 경우
# 아홉 난쟁이가 주어졌을 때 일곱 난쟁이의 키의 합이 100이 되어야 함
# 이 경우의 키를 오름차순으로 출력

import sys
from itertools import combinations
input = sys.stdin.readline

height = [int(input().rstrip()) for _ in range(9)]

comb = combinations(height, 7)


for c in comb :
    if sum(c) == 100 :
        answer = c

answer = sorted(answer)
for i in answer :
    print(i)



