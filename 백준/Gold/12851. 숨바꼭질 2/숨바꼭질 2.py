# 숨바꼭질2. 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다.
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
#
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
#
# 출력
# 첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
#
# 둘째 줄에는 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력한다.

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())


def bfs() :
    q = deque()
    q.append(N)
    dist = [0 for _ in range(100001)] # 각 위치까지 도달하는데 필요한 시간

    time = 0
    cnt = 0
    while q :
        x = q.popleft()
        if x == K : # K에 도착
            time = dist[x]
            cnt += 1
            continue

        for nx in (x+1, x-1, x*2) : # 한칸씩 걸어가는 경우와 순간이동한 경우
            if 0 <= nx < 100001 and (dist[nx] == 0 or dist[nx] == dist[x]+1) : # 방문하지 않았거나 동일한 방문횟수면 탐색
                dist[nx] = dist[x]+1 
                q.append(nx)

    print(time)
    print(cnt)

bfs()





