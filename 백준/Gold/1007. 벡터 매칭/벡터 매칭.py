# 벡터 매칭. 평면 상에 N개의 점이 찍혀있고, 그 점을 집합 P라고 하자.
# 집합 P의 벡터 매칭은 벡터의 집합인데, 모든 벡터는 집합 P의 한 점에서 시작해서, 또 다른 점에서 끝나는 벡터의 집합이다. 또, P에 속하는 모든 점은 한 번씩 쓰여야 한다.
# 벡터 매칭에 있는 벡터의 개수는 P에 있는 점의 절반이다.
# 평면 상의 점이 주어졌을 때, 집합 P의 벡터 매칭에 있는 벡터의 합의 길이의 최솟값을 출력하는 프로그램을 작성하시오.
#
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 구성되어있다.
# 테스트 케이스의 첫째 줄에 점의 개수 N이 주어진다. N은 짝수이다. 둘째 줄부터 N개의 줄에 점의 좌표가 주어진다. N은 20보다 작거나 같은 자연수이고, 좌표는 절댓값이 100,000보다 작거나 같은 정수다. 모든 점은 서로 다르다.
# 각 테스트 케이스마다 정답을 출력한다. 절대/상대 오차는 10-6까지 허용한다.

import sys
import math
from itertools import combinations
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T) :
    N = int(input().rstrip())

    # 모든 좌표들의 총 합
    points = []
    totalX, totalY = 0, 0

    for _ in range(N) :
        x, y = map(int, input().rstrip().split())
        totalX += x
        totalY += y
        points.append([x, y])

    result = sys.maxsize
    comb = list(combinations(points, int(N/2)))
    length = int(len(comb) / 2) # 조합을 절반만 해도 됨

    for su in comb[:length] :
        su = list(su)

        # 더하는 좌표 총 합
        totalX1, totalY1 = 0, 0
        for x1, y1 in su :
            totalX1 += x1
            totalY1 += y1

        # 빼야하는 좌표 총 합 = 모든 좌표 총 합 - 더해야하는 좌표 총합
        totalX2 = totalX - totalX1
        totalY2 = totalY - totalY1

        result = min(result, math.sqrt((totalX1 - totalX2)**2 + (totalY1 - totalY2)**2))

    print(result)




