# M, N, H 토마토. 익은 곳이 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향으로 퍼젼감
# 토마토가 모두 익을 때까지 걸리는 최소 일 수는?
# 1은 익은 토마토, 0은 익지 않은 토마토, -1은 빈칸

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0] # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, input().rstrip().split())

arr = [[list(map(int, input().rstrip().split())) for _ in range(N)] for _ in range(H)]
q = deque()

for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if arr[i][j][k] == 1 :
                q.append((i, j, k))
# 3차원 bfs?

while q :
    x, y, z = q.popleft()

    for d in range(6) :
        nx = x + dx[d]
        ny = y + dy[d]
        nz = z + dz[d]

        if 0<=nx<H and 0<=ny<N and 0<=nz<M and arr[nx][ny][nz] == 0 :
            q.append((nx, ny, nz))
            arr[nx][ny][nz] = arr[x][y][z] + 1 # 며칠 걸리는지


day = 0
for i in arr : # 하나라도 익지 않은 토마토가 있으면 -1 출력
    for j in i :
        for k in j :
            if k == 0 :
                print(-1)
                exit(0)
        day = max(day, max(j))
print(day-1) # day가 1일차부터

