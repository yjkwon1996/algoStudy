# LCS(최장 공통 부분 수열) : 두 수열이 주어졌을 때 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제
# ex) ACAYKP, CAPCAK -> ACAK

import sys
input = sys.stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()

dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

for i in range(1, len(word1)+1) :
    for j in range(1, len(word2)+1) :
        if word1[i-1] == word2[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(word1)][len(word2)])
