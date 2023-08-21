# 삼각형의 크기 n이 주어지면
# 맨 위층부터 아래층까지 가면서 합이 최대가 되는 경로를 찾기

import sys
input = sys.stdin.readline

n = int(input())

dp = []
# 입력을 받으면서, 각각의 두 가지 경우를 나눠서 생각
for _ in range(n) :
    dp.append(list(map(int, input().rstrip().split())))

# 합의 최댓값을 찾아가는 과정
for i in range(1, n) : # 맨 위층은 생략
    for j in range(len(dp[i])) : # 각 층별로 길이가 다르므로(1 - 2 - 3 - 4 ...)
        if j == 0 : # 삼각형에서 처음과 마지막은 선택지가 없음
            dp[i][j] = dp[i][j] + dp[i-1][j]
        elif j == len(dp[i])-1 :
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
        else : # 다른 부분은 좌우에서 큰 값을 선택할 수 있음
            dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1])) # 마지막 층에서 최댓값을 찾아서 출력


