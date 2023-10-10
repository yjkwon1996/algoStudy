# 오큰수. 크기가 N인 수열 A, 수열에 각 원소에 대해서 오큰수 구하기
# Ai의 오큰수 : 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수. 없으면 -1

import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 수열 A의 크기
A = list(map(int, input().rstrip().split()))

answer = [-1 for _ in range(N)] # 갱신 안되면 -1
stack = []

stack.append(0)
for i in range(N) :
    while stack and A[stack[-1]] < A[i] : # 오큰수가 있다면
        answer[stack.pop()] = A[i]
    stack.append(i)

for i in range(N) :
    print(answer[i])
