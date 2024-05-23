import heapq
import sys
def solution(N, road, K):
    answer = 0
    arr = [[] for _ in range(N+1)]
    distance = [sys.maxsize for _ in range(N+1)]
    distance[1] = 0

    for a, b, c in road :
        arr[a].append((b, c))
        arr[b].append((a, c))

    h = [(0, 1)] # 힙

    while h :
        dist, now = heapq.heappop(h)

        if distance[now] < dist : # 더 길면 볼필요X
            continue

        for nextNode, nextDist in arr[now] :
            distSum = dist + nextDist
            if distance[nextNode] > distSum :
                distance[nextNode] = distSum
                heapq.heappush(h, (distSum, nextNode))

    for dist in distance[1:] :
        if dist <= K :
            answer += 1

    return answer