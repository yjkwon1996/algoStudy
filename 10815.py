# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/10815
# 10815 숫자 카드

# 집합과 맵

"""

# 시간초과

N = int(input()) # 상근이가 가지고 있는 카드의 수
arr = list(map(int, input().split())) # 숫자 카드에 적혀 있는 숫자
M = int(input()) # 상근이가 가진 수의 카드인지 아닌지 판별해야 할 카드의 수
arr2 = list(map(int, input().split())) # 상근이가 가지고있는 숫자 카드인지 아닌지를 구해야 할 정수 M개


answer = []

# 가지고 있으면 1, 없으면 0
for i in arr2 :
    if i in arr :
        answer.append(1)
    else : 
        answer.append(0)

print(*answer)

"""

# 시간초과 - 이진탐색

N = int(input()) # 상근이가 가지고 있는 카드의 수
arr = list(map(int, input().split())) # 숫자 카드에 적혀 있는 숫자
M = int(input()) # 상근이가 가진 수의 카드인지 아닌지 판별해야 할 카드의 수
arr2 = list(map(int, input().split())) # 상근이가 가지고있는 숫자 카드인지 아닌지를 구해야 할 정수 M개

arr = sorted(arr) # 이진탐색을 위한 정렬
answer = []
# 이진탐색
def bina(value, start, end) : # value 값을 찾기 위한 이진탐색
    mid = (start+end) // 2
    if start > end : # 탐색 다 했는데 없으면
        answer.append(0)
    elif value == arr[mid] : # 있으면
        answer.append(1)
    elif value > arr[mid] : # 다음 탐색. 현재보다 큰 값이라면
        bina(value, mid+1, end)
    else :
        bina(value, start, mid-1) # 현재보다 더 작은 값이라면

# 가지고 있으면 1, 없으면 0
for i in arr2 :
    start = 0
    end = len(arr) - 1
    bina(i, start, end)

print(*answer)
