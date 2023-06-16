# N, M 행렬
# 0은 이동가능, 1은 이동불가
# (1, 1)에서 (N, M)으로 이동하는 최단경로
# 벽을 한 개까지 부수고 이동할 수 있음
# 벽을 깬 경우의 bfs와 벽을 깨지 않은 bfs를 돌리면?
from collections import deque

dx = [1, 0, -1, 0] # 우 하 좌 상
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)] # 3차원 행렬(행, 열, 벽을 깬 여부)

# wall_break : 0 -> 벽을 부수지 않고 이동한 경우, 1 -> 벽을 부수고 이동한 경우 
def bfs(wall_break, visited, arr) :
    q = deque()
    q.append((0, 0, wall_break))
    visited[0][0][wall_break] = 1
    
    while q :
        x, y, wall_break = q.popleft()
        
        if x == N-1 and y == M-1 : # 도착
            return visited[x][y][wall_break] # 최단거리 리턴
        
        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx<0 or nx>=N or ny<0 or ny>=M : # 범위 밖이면 탐색X
                continue
            
            if arr[nx][ny] == 0 and visited[nx][ny][wall_break] == 0 : # 벽을 부수지 않고 이동
                q.append((nx, ny, wall_break))
                visited[nx][ny][wall_break] = visited[x][y][wall_break] + 1 # 이동거리
                
            if arr[nx][ny] == 1 and wall_break == 0 : # 벽을 부수고 이동
                q.append((nx, ny, 1))
                visited[nx][ny][1] = visited[x][y][wall_break] + 1
    
    return -1 # 큐를 모두 돌았는데 도착점에 도착하지 못한 경우

print(bfs(0, visited, arr))
