# 빙산. 한 덩어리의 빙산이 주어질 때, 바닷물과 인접한 부분은 동서남북으로 바닷물과 붙어있는 만큼 줄어든다.
# 한 덩어리의 빙산이 녹아서 두 덩어리 이상으로 분리되는 최초의 시간을 구하기

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) # 행과 열
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

# bfs
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(x, y) :
    q = deque([(x, y)])
    visited[x][y] = 1
    melt = [] # 1 이상의 위치를 넣어두고 나중에 꺼내면서 1씩 낮추기

    while q :
        x, y = q.popleft()
        sea = 0 # 주변의 바다 갯수를 파악

        for d in range(4) : # 4면 탐색하면서 바다가 있으면 sea+1, 육지가 있으면 큐에 넣어서 더 탐색
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M :
                if not arr[nx][ny] :
                    sea += 1
                elif arr[nx][ny] and not visited[nx][ny] :
                    visited[nx][ny] = 1
                    q.append((nx, ny))

        if sea > 0 :
            melt.append((x, y, sea))

    # 녹여야 되는 부분을 처리
    for x, y, sea in melt :
        arr[x][y] = max(0, arr[x][y] - sea) # 단순히 -만 하는게 아니라, 이후 계산을 위해 0 이하는 0으로 설정

    return 1

# 빙산이 있는 위치만 탐색
land = []
for i in range(N) :
    for j in range(M) :
        if arr[i][j] :
            land.append((i, j))

year = 0
while land :
    visited = [[0 for _ in range(M)] for _ in range(N)]
    seaList = []

    island = 0
    for x, y in land :
        if arr[x][y] and not visited[x][y] :
            island += bfs(x, y)

        # 탐색을 끝내면 바다가 된 빙산이 있는지 체크.
        if arr[x][y] == 0 :
            seaList.append((x, y))

    if island > 1 :
        print(year)
        break

    for point in seaList :
        land.remove(point)

    year += 1

# 마지막까지 탐색했는데 섬이 2개 이상으로 안 나눠지면 0 출력
if island < 2 :
    print(0)








