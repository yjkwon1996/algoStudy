# 2×n 타일링 2. 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

import sys
input = sys.stdin.readline

# n=1 -> 1 / n=2 -> 3 / n=3 -> 5 / n=4 -> 11 ...
# i = i-1의 그림과, (i-2)*2의 그림의 합
# dp[i] = dp[i-1] + dp[i-2] * 2

n = int(input().rstrip())
dp = [0 for _ in range(n+1)]
dp[0] = 1
dp[1] = 3
for i in range(2, n) :
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[n-1] % 10007)
