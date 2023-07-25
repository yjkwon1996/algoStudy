# 2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 10007로 나눈 나머지를 구하기

import sys
input = sys.stdin.readline

n = int(input())

# 각각의 경우의 수는 피보나치
# dp로 계산
dp = [0, 1, 2] # 2x0, 2x1, 2x2의 각각의 경우의 수

for i in range(3, n+1) :
    dp.append(dp[i-1] + dp[i-2])

print(dp[n] % 10007)


