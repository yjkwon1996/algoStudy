from collections import deque
import sys

dy = [0, 1, 0, -1] # 우하좌상
dx = [1, 0, -1, 0]

def bfs(board, direction) :
    n = len(board)
    cost = [[sys.maxsize] * n for _ in range(n)] # 비용 dp겸 방문체크역할도 해줌
    cost[0][0] = 0
    
    q = deque()
    q.append((0, 0, 0, direction)) # (시작x, 시작y, 시작cost, 시작direction)
    
    while q :
        x, y, c, dir = q.popleft()
        if x == n-1 and y == n-1 : # 목적지에 도달
            continue
        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]
            ndir = d
            
            if nx<0 or ny<0 or nx>=n or ny>=n or board[ny][nx] == 1 : # 맵 밖이거나 벽이면
                continue
                
            if dir == ndir : # 같은 방향이면 100원만
                nc = c + 100
            else : # 다른 방향이면 600원(코너 값 + 직진 값)
                nc = c + 600
                
            # 이전에 계산한 값보다 더 싸게 이동할 수 있다면 큐에 넣고 다시 계산
            if nc < cost[ny][nx] :
                cost[ny][nx] = nc
                q.append((nx, ny, nc, ndir))
                
    return cost[-1][-1]

def solution(board):
    answer = min(bfs(board, 0), bfs(board, 1)) # 처음에 오른쪽 or 아래쪽 이동의 최소비용
    
    return answer