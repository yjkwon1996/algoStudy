# 정수 n이 주어졌을 때 n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하기
# 순서 상관 있음
# dp?

import sys

input = sys.stdin.readline

T = int(input())


def dp(n):
    if n == 1:  # 1
        return 1
    elif n == 2:  # 2 / 1, 1
        return 2
    elif n == 3:  # 3 / 2, 1 / 1, 2 / 1, 1, 1
        return 4
    else:
        return dp(n - 1) + dp(n - 2) + dp(n - 3)


for _ in range(T):
    n = int(input())
    print(dp(n))
