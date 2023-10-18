# 가운데를 말해요. 수를 하나씩 외칠때마다 지금까지 말한 수 중에서 중간값을 말해야 한다
# 1, 5, 2, 10, -99, 7, 5 -> 1, 1, 2, 2, 2, 2, 5
# 값을 minHeap과 maxHeap에 번갈아 넣어 줌으로써 두 힙의 균형을 유지해서 pop하면 바로 중간값이 나오도록

import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())

minHeap = [] # 중간값보다 작은 값
maxHeap = [] # 중간값보다 큰 값

for _ in range(N) :
    number = int(input().rstrip())

    if len(minHeap) == len(maxHeap) :
        heapq.heappush(maxHeap, -number)
    else :
        heapq.heappush(minHeap, number)

    if minHeap and minHeap[0] < -maxHeap[0] : # maxHeap에 원소를 넣을 때 minHeap보다 작은 값이 들어가면 maxHeap에 중간값보다 큰 원소가 들어가게 됨
        maxValue = heapq.heappop(maxHeap) # 따라서 값을 교정해줘야함
        minValue = heapq.heappop(minHeap)

        heapq.heappush(maxHeap, -minValue)
        heapq.heappush(minHeap, -maxValue)

    print(-maxHeap[0])

