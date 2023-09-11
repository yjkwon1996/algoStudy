# 최소비용 구하기 - N개의 도시가 있고, 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스
# A 도시에서 B 도시까지 가는데 드는 버스 비용을 최소화
# 최단경로 - 다익스트라?

import sys
import heapq

input = sys.stdin.readline

N = int(input()) # 도시의 수
M = int(input()) # 버스의 수

bus = [[] for _ in range(N+1)] # 버스 정보
for _ in range(M) :
    s, e, c = map(int, input().rstrip().split()) # 시작지, 목적지, 비용
    bus[s].append([e, c])

start, end = map(int, input().rstrip().split()) # 도시의 출발점 A와 도착지점 B

dist = [sys.maxsize for _ in range(N+1)] # 초기값은 최댓값으로 설정
dist[start] = 0

q = [[0, start]] # 시작 노드부터 집어넣고 탐색 시작. 우선순위 큐로 큐를 이용

while q :
    d, n = heapq.heappop(q) # 거리와 노드

    if d > dist[n] : # 기존 값보다 멀다면 X
        continue

    # 기존 값보다 멀지 않다면 계산
    for nNode, nDist in bus[n] :
        cost = dist[n] + nDist # 인접 노드까지의 거리가
        if cost < dist[nNode] : # 기존에 계산한 거리보다 짧으면 갱신
            dist[nNode] = cost
            heapq.heappush(q, [cost, nNode])


print(dist[end])



