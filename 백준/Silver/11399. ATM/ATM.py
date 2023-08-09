# 1대의 ATM을 N명이서 사용하려고 할 때 각 사람이 돈을 인출할 때 필요로 하는 시간의 합의 최솟값

import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().rstrip().split()))

# 정렬해서 하면 될듯

P.sort()

sum = 0
answer = 0
for i in P :
    sum += i
    answer += sum

print(answer)