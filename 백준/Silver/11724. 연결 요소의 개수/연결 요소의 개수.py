# 방향 없는 그래프가 주어졌을 때 연결 요소의 개수 구하기

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split()) # 정점의 개수 N과 간선의 개수 M
graph = [[] for _ in range(N+1)]

# 연결된 그래프들을 모두 확인하기 위한 dfs
def dfs(x, depth) :
    visited[x] = True

    for i in graph[x] :
        if not visited[i] :
            dfs(i, depth+1)

# 방향 없는 그래프 - 양방향
for _ in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = 0
visited = [False for _ in range(N+1)]

# 1번 노드부터 시작(0 아님)
for i in range(1, N+1) :
    if not visited[i]: # 아직 방문안한 곳이
        if not graph[i] : # 연결된 곳이 없는 단일 노드라면
            answer += 1
            visited[i] = True
        else : # 연결된 곳이 있다면 dfs 탐색
            answer += 1
            dfs(i, 0)

print(answer)
