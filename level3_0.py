from collections import deque
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

def move(pos1, pos2, new_board) :
    x = 1
    y = 0
    arr = []
    # 이동
    mv = [(-1, 0), (0, 1), (1, 0), (-1, 0)]
    for y2, x2 in mv :
        next_pos1 = (pos1[y] + y2, pos1[x] + x2)
        next_pos2 = (pos2[y] + y2, pos2[x] + x2)
        if new_board[next_pos1[y]][next_pos2[x]] == 0 and new_board[next_pos2[y]][next_pos2[x]] == 0 :
            arr.append((next_pos1, next_pos2))
        # 회전
        if pos1[y] == pos2[y] : # 가로 방향 회전
            for i in [-1, 1] : # -1 : 위로, 1 : 아래로
                if new_board[pos1[y]+i][pos1[x]] == 0 and new_board[pos2[y]+i][pos2[x]] == 0 :
                    arr.append((pos1, (pos1[y]+i, pos1[x])))
                    arr.append((pos2, (pos2[y]+i, pos2[x])))
        else : # 세로 방향 회전
            for i in [-1, 1] : # -1 : 왼쪽, 1 : 오른쪽
                if new_board[pos1[y]][pos1[x]+i] == 0 and new_board[pos2[y]][pos2[x]+i] == 0 :
                    arr.append((pos1, (pos1[y], pos1[x]+i)))
                    arr.append((pos2, (pos2[y], pos2[x]+i)))
        return arr


def solution(board) :  
    """
    0과 1로 이루어진 지도 board
    로봇이 (N,N) 위치까지 이동하는데 필요한 최소 시간을 return
    로봇은 2x1 크기, 가장 왼쪽, 상단의 좌표는 (1, 1)
    0은 빈칸, 1은 벽. 벽이 회전이 가능하지만 벽에 영향을 받음
    """
    
    N = len(board)
    
    # 외벽이 1로 만들어져 있는 new_board
    new_board = [[1] * (N+2) for _ in range(N+2)]
    for i in range(N) :
        for j in range(N) :
            new_board[i+1][j+1] = board[i][j]
    
    q = deque([((1, 1), (1, 2), 0)]) # 현재 좌표 위치 큐
    check = set([((1, 1), (1, 2))]) # 이미 방문한 곳을 확인하기 위해
    
    while q : 
        pos1, pos2, cnt = q.popleft()
        if pos1 == (N, N) or pos2 == (N, N) :
            return cnt
        for next_position in move(pos1, pos2, new_board) :
            if next_position not in check :
                q.append((*next_position, cnt+1))
                check.add(next_position)
        
   
# 이게 아닌거 같은데...