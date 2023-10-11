# 최소 힙. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
# 배열에 자연수 x를 넣는다.
# 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.

import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip()) # 연산의 개수

heap = []
for _ in range(N) :
    x = int(input())

    if x == 0 :  # x가 0이라면 배열에서 가장 작은 값을 출력
        if not heap : # 비어있는 배열인데 가장 작은 값을 출력하라고 하는 경우, 0 출력
            print(0)
        else :
            print(heapq.heappop(heap))

    else : # x가 자연수라면 배열에 x라는 값을 추가하는 연산
        heapq.heappush(heap, x)







