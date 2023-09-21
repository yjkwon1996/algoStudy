# 방향이 없는 그래프. 1번 정점에서 N번 정점으로 이동.
# 임의로 주어진 두 정점은 반드시 통과하는 최단 경로의 길이를 출력

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N, E = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]

for _ in range(E) :
    # 방향성이 없는 그래프
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().rstrip().split())

def dijkstra(s, e) : # 출발점에서 목적지로 가는 최단 경로
    dist = [INF for _ in range(N+1)]
    dist[s] = 0

    q = []
    heapq.heappush(q, (0, s))
    while q :
        distance, point = heapq.heappop(q)
        if distance > dist[point] : # 더 길면 X
            continue

        for nPoint, value in graph[point] :
            if dist[point] + value < dist[nPoint] : # 현재 정점의 거리를 더한 값이 더 작으면
                dist[nPoint] = dist[point] + value # 값 갱신
                heapq.heappush(q, (dist[nPoint], nPoint))

    return dist[e]

# 임의의 두 정점을 통과해야 함 -> 시작점에서 v1, v1에서 v2, v2에서 N 각각의 최단거리를?

answer1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
# v2를 먼저 가는 경우도 확인해야함
answer2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

# print(dijkstra(1, v2), dijkstra(v2, v1), dijkstra(v1, N))
# print(answer1, answer2)

if answer1 >= INF and answer2 >= INF :
    print(-1)
else :
    print(min(answer1, answer2))



