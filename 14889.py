# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/14889
# 14889 스타트와 링크

"""

# 시간초과

import math

def dfs(idx, depth) :
    global answer
    if depth == N // 2 : # 선수를 둘로 나눠서(두 팀이 완성될 정도로 depth를 반복했다면)
        value1 = 0 # 스타트팀의 점수
        value2 = 0 # 링크팀의 점수
        for i in range(N) :
            for j in range(N) :
                if visited[i] and visited[j] : # i 팀원과 j 팀원이 한팀(스타트팀)에 있다면 값 추가
                    value1 += arr[i][j]
                elif not visited[i] and not visited[j] : # 혹은 둘 모두가 같은 팀에 없다면 링크팀에 추가
                    value2 += arr[i][j]
        answer = min(answer, abs(value1-value2)) # 이후 최소값 갱신
        return
    
    for i in range(idx, N) :
        if not visited[i] :
            visited[i] = True # 배정되지 않은 선수라면 배정
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
    start_team = team_comb[i] # 절반은 스타트팀
    value1 = 0
    for j in range(N // 2) : # 스타트팀의 멤버를 구하고, 그 값을 찾아서 추가
        member = start_team[j]
        for k in start_team :
            value1 += arr[member][k]
            
    link_team = team_comb[-i-1] # 절반은 링크팀
    value2 = 0
    for j in range(N // 2) : # 링크팀의 멤버를 구하고, 그 값을 찾아서 추가
        member = start_team[j]
        member = link_team[j]
        for k in link_team :
            value2 += arr[member][k]
    
    answer = min(answer, abs(value1-value2))

print(answer)





