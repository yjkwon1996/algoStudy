# 자연수 N이 주어지면 N길이의 이진 수열을 만들기. 단, 0은 단독으로 존재할 수 없고 00으로 가능. 15746으로 나눈 나머지를 출력
# N이 주어졌을 때 만들 수 있는 경우의 수

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(1000001)]

dp[1] = 1
dp[2] = 2

# 1 - 1 / 2 - 00, 11 / 3 - 001, 100, 111 / 4 - 0011, 0000, 1100, 1001, 1111
# 1 2 3 5 8 ... -> (n-1) + (n-2)

for i in range(3, N+1) :
    dp[i] = (dp[i-1] + dp[i-2]) % 15746 # 메모리 초과

print(dp[N])



