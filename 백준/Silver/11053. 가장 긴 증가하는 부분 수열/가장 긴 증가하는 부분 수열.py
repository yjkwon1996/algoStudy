# 수열 A가 주어졌을 때 가장 긴 증가하는 부분 수열을 구하기
# 그 길이를 출력

import sys
input = sys.stdin.readline

N = int(input()) # 수열 A의 크기
A = list(map(int, input().split()))

# 증가하는 수열 찾기
dp = [0 for _ in range(N)] # 수열의 길이를 dp로

for i in range(N) :
    for j in range(i) :
        if A[i] > A[j] and dp[i] < dp[j] : # 더 긴 수열 발견
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp)) # dp[-1]이 아님. A[i]와 A[j]를 비교하고 있어서