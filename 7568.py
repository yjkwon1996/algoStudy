# 7568 덩치
# https://www.acmicpc.net/problem/7568

"""
사람의 덩치를 키와 몸무게 두개의 값으로 표현하여 그 등수를 매겨보려고 한다.
어떤 사람의 몸무게가 x kg, 키가 y cm이라면 이사람의 덩치는 (x, y)
두 사람 A, B의 덩치가 각각 (x, y), (p, q)라고 할 때
x > p, y > q라면 A의 덩치가 B보다 크다.
하지만 키는 작지만 몸무게가 작거나, 그 반대인 경우 등에서 덩치를 비교하기 어렵다.
N명의 집단에서 각 사람의 덩치 등수. 자신보다 덩치가 큰 사람이 k명이면 그 사람의 덩치 등수는 k + 1
같은 덩치 등수를 가진 사람이 여럿일 수 있음

전체 사람의 수 N이 주어진다. 이후 N개의 줄에서 각 사람의 몸무게와 키를 나타내는 양의 정수 x, y가 하나의 공백을 두고
출력 : 입력에 나열된 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력하되 공백으로 구분
"""

N = int(input())

height = []
weight = []
for _ in range(N) :
    x, y = map(int, input().split())
    height.append(x)
    weight.append(y)

# 자기보다 크고 무거운 사람이 몇명 있는지 확인하고, 자신의 등수를 체크하면 된다.

for i in range(N) :
    rank = 1 # 등수
    
    for j in range(N) :
        if height[i] < height[j] and weight[i] < weight[j] :
            rank += 1
    print(rank, end=' ')


    