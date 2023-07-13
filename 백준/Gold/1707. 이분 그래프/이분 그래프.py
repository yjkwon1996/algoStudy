# 그래프의 정점의 집합을 둘로 분리하여 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때 -> 이분 그래프.
# 그래프가 주어졌을 때 이분 그래프인지 아닌지 판별
# 노드 연결 후, dfs로 판별?

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

K = int(input())  # 테스트케이스

def dfs(s, arr) :
    visited[s] = arr # 해당정점의 집합

    for i in g[s] : # 해당 집합의 그래프를 확인
        if not visited[i] : # 아직 방문하지 않은 정점을
            a = dfs(i, -arr) # 다른 집합의 값으로 dfs
            if not a : # dfs한 결과에서 False가 나왔다면 -> 이분 그래프가 아님
                return False
        elif visited[i] == visited[s] : # 현재 정점과 연결된 정점이 같은 집합이라면 -> 이분 그래프가 아님
            return False
    return True

for _ in range(K) :
    V, E = map(int, input().split())
    g = [[] for _ in range(V+1)] # 빈 그래프
    visited = [False] * (V+1) # 방문한 곳 확인용

    for _ in range(E) :
        u, v = map(int, input().split()) # 그래프 그리기
        g[u].append(v)
        g[v].append(u)

    for i in range(1, V+1) :
        if not visited[i] : # 아직 방문하지 않은 정점을 모두 dfs로 확인해야함
            answer = dfs(i, 1)
            if not answer : # 그 결과값이 하나라도 이분 그래프가 아니라면, 더 확인할 필요 X
                print("NO")
                break
    if answer :
        print("YES")
