# 0과 1로만 이루어진 이진수 중 특별한 성질을 가지는 것을 이친수라고 함
# 0으로 시작하지 않으면서, 1이 두번 연속으로 나타나지 않음
# N이 주어졌을 때 N자리 이친수의 개수를 구하기

import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+1)]

if N == 1 :
    print(1)
    sys.exit()
elif N == 2 :
    print(1)
    sys.exit()

# 1 / 10 / 100, 101 / 1000, 1001, 1010 / 10000, 10001, 10010, 10100, 10101
# 1 1 2 3 5 ...
dp[1] = 1
dp[2] = 1

for i in range(3, N+1) :
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])

