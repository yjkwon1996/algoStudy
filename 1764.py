# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1764
# 1764 듣보잡


"""
# 시간초과
# 듣도 못한사람, 보도 못한 사람
N, M = map(int, input().split())

hear = []
see = []
for i in range(N) :
    hear.append(input())

for j in range(M) :
    see.append(input())

# 듣도 보도 못한 사람 출력
answer = []
for i in hear :
    if i in see :
        answer.append(i)

answer = sorted(answer)
print(len(answer))
print(*answer, sep='\n')

"""


# 듣도 못한사람, 보도 못한 사람
N, M = map(int, input().split())

hear = set() # 집합으로 시간 줄임
see = set()
for i in range(N) :
    hear.add(input())

for j in range(M) :
    see.add(input())

# 듣도 보도 못한 사람 출력
answer = list(hear & see) # 두 집합에 모두 존재하는(교집합)
answer = sorted(answer)
print(len(answer))
print(*answer, sep='\n')

"""
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

"""