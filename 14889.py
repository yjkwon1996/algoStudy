# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/14889
# 14889 스타트와 링크

"""
# 시간초과

import math

def dfs(idx, depth) :
    global answer
    if depth == N // 2 :
        value1 = 0
        value2 = 0
        for i in range(N) :
            for j in range(N) :
                if visited[i] and visited[j] :
                    value1 += arr[i][j]
                elif not visited[i] and not visited[j] :
                    value2 += arr[i][j]
        answer = min(answer, abs(value1-value2))
        return
    
    for i in range(idx, N) :
        if not visited[i] :
            visited[i] = True
            dfs(depth+1, idx+1)
            visited[i] = False


N = int(input()) # 사람의 수, 항상 짝수
arr= [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)] # 방문 했는지 확인용
answer = math.inf

dfs(0, 0)

print(arr)

"""

# combinations 사용시
        
from itertools import combinations
import math

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
team = [i for i in range(N)]
team_comb = []

# 조합 가능한 팀
for i in list(combinations(team, N // 2)) :
    team_comb.append(i)
    
answer = math.inf
for i in range(len(team_comb) // 2) :
    start_team = team_comb[i]
    value1 = 0
    for j in range(N // 2) :
        member = start_team[j]
        for k in start_team :
            value1 += arr[member][k]
            
    link_team = team_comb[-i-1]
    value2 = 0
    for j in range(N // 2) :
        member = link_team[j]
        for k in link_team :
            value2 += arr[member][k]
    
    answer = min(answer, abs(value1-value2))

print(answer)

    



