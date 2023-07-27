# 1부터 n까지의 포도주 잔과 각 포도주 잔에 들어 있는 포도주의 양이 주어졌을 때
# 가장 많은 양의 포도주를 마실 때 그 포도주의 양을 출력
# 한 번 고르면  모두 다 마시고, 연속으로 놓여있는 3잔을 마실 수는 없음


import sys
input = sys.stdin.readline

n = int(input()) # 포도주 잔의 개수
wine = []
for _ in range(n) :
    wine.append(int(input()))

# dp로 포도주를 가장 많이 마실 수 있는 경우를 찾기

if n < 3 : # 포도주 잔의 개수가 세개 미만의 경우
    print(sum(wine))
    sys.exit()

dp = [0 for _ in range(n)]
dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(dp[1], wine[0] + wine[2], wine[1] + wine[2])

# 3연속이 불가능한 조합에서 최대값 찾기
for i in range(3, n) :
    dp[i] = max(dp[i-2] + wine[i], dp[i-3] + wine[i] + wine[i-1], dp[i-1])

print(max(dp))