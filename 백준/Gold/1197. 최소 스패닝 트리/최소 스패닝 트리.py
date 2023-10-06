# 최소 스패닝 트리
# 그래프가 주어졌을 때 최소 스패닝 트리(주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중 가중치의 합이 최소인 트리)를 구하기

import sys
input = sys.stdin.readline

V, E = map(int, input().rstrip().split()) # 정점의 개수 V, 간선의 개수 E

# A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있음
graph = [list(map(int, input().rstrip().split())) for _ in range(E)]
parent = [i for i in range(V+1)]

# 유니온파인드?
graph.sort(key=lambda x : x[2]) # 가중치 기준으로 정렬해서 최소 트리 찾기

def find(x) :
    if x == parent[x] :
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(x, y) :
    x = find(x)
    y = find(y)

    if x > y :
        parent[x] = y
    else :
        parent[y] = x

answer = 0
for a, b, c in graph :
    if find(a) != find(b) : # 부모 노드가 같지 않다면 스패닝 트리
        union(a, b)
        answer += c

print(answer)


