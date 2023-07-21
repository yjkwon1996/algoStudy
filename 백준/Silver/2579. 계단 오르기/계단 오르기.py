# 계단 오르기. 한 번에 한 계단씩 또는 두 계단씩 오를 수 있음. 밟은 계단의 점수를 얻는 형식
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단 시작점은 계단에 포함 X
# 마지막 도착 계단은 반드시 밟아야 함. 위 상황에서 이 게임에서 얻을 수 있는 총 점수의 최댓값은?

import sys
input = sys.stdin.readline

N = int(input()) # 계단의 개수
stairs = [int(input()) for _ in range(N)] # 계단 점수
dp = [0 for _ in range(N)]

if len(stairs) <= 2 : # 계단이 2 이하면 모두 다 올라가서 점수 획득
    print(sum(stairs))
else : # 계단이 3개 이상이면 dp
    dp[0] = stairs[0]
    dp[1] = dp[0] + stairs[1]
    for i in range(2, N) : # 한 계단을 오르는 경우와 두 계단을 오르는 경우를 dp로
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    print(dp[-1])


