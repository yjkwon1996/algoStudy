# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/14425
# 14425 문자열 집합

"""

# 이것도 되지만 시간이...

N, M = map(int, input().split()) # 문자열의 개수

# N개의 줄에는 집합 S에 포함되어 있는 문자열
arr_N = []
for i in range(N) :
    arr_N.append(input())

# M개에는 검사해야 하는 문자열
arr_M = []
for i in range(M) :
    arr_M.append(input())

cnt = 0
for i in arr_M :
    if i in arr_N :
        cnt += 1

print(cnt)

"""

"""
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink
"""

# 중복 없으므로 set?

N, M = map(int, input().split()) # 문자열의 개수

# N개의 줄에는 집합 S에 포함되어 있는 문자열
S = set([input() for _ in range(N)])

# M개에는 검사해야 하는 문자열
cnt = 0
for _ in range(M): # M개의 줄에 입력한 문자열이 집합S에 포함된다면
    if input() in S :
        cnt += 1

print(cnt)


