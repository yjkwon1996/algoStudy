# 타일 채우기. 3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.
#
# 출력
# 첫째 줄에 경우의 수를 출력한다.

import sys
input = sys.stdin.readline

N = int(input().rstrip())

dp = [0 for _ in range(32)]
dp[2] = 3
for i in range(4, N+1) :
    if i%2 == 1 : # 홀수(3x3, 3x5, 3x7 ...은 불가능)
        dp[i] = 0
    else :
        dp[i] = (dp[i-2]*3) + (sum(dp[:i-2]) * 2) + 2

print(dp[N])

