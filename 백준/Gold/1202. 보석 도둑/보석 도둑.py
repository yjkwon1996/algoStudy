# 보석 도둑. 세계적인 도둑 상덕이는 보석점을 털기로 결심했다.
#
# 상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.
#
# 상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)
#
# 다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)
#
# 다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)
#
# 모든 숫자는 양의 정수이다.
#
# 출력
# 첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.

import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

jewel = []
for _ in range(N) :
    heapq.heappush(jewel, list(map(int, input().rstrip().split())))

bag = [int(input().rstrip()) for _ in range(K)]
bag.sort()
answer = 0
tmp = []

# 작은 가방부터 확인하면서 최대 가치의 보석을 담기
for b in bag :
    while jewel and b >= jewel[0][0] : # 가방에 아무보석도 못담으면 끝
        heapq.heappush(tmp, -heapq.heappop(jewel)[1])

    if tmp :
        answer -= heapq.heappop(tmp)
    elif not jewel :
        break

print(answer)


