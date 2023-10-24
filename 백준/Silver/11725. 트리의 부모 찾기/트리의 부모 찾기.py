# 트리의 부모 찾기. 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().rstrip())
graph = [[] for i in range(N+1)]

for i in range(N-1) :
    s, e = map(int, input().rstrip().split())
    graph[s].append(e) # 양방향으로
    graph[e].append(s)

parent = [0 for _ in range(N+1)] # 각 노드의 부모값을 저장

# dfs 방식으로 각 노드의 부모를 찾아서 올라감
def dfs(x) :
    for i in graph[x] :
        if not parent[i] :
            parent[i] = x
            dfs(i)

dfs(1) # 1부터 시작

for i in range(2, N+1) :
    print(parent[i])



