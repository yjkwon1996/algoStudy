# 구슬 탈출 2. 스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다.
# 구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.
# 보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다. 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다.
# 빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다. 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.
# 이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다. 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.
# 각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다. 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다.
# 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.
# 보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.
# 입력
# 첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다. 다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다.
# 이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다. '.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 'O'는 구멍의 위치를 의미한다.
# 'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.
# 입력되는 모든 보드의 가장자리에는 모두 '#'이 있다. 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.
# 출력
# 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다. 만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.

import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, input().rstrip().split()) # 가로 M, 세로 N
board = []
for i in range(N) :
    board.append(list(input().rstrip()))
    for j in range(M) :
        if board[i][j] == 'R' :
            rx, ry = i, j
        elif board[i][j] == 'B' :
            bx, by = i, j

visited = []
def bfs(rx, ry, bx, by) :
    q = deque()
    q.append((rx, ry, bx, by))
    visited.append((rx, ry, bx, by))

    cnt = 0
    while q :
        if cnt > 10 :
            print(-1)
            return

        for _ in range(len(q)) :
            rx, ry, bx, by = q.popleft()
            visited.append((rx, ry, bx, by))

            if board[rx][ry] == 'O' :
                print(cnt)
                return

            for d in range(4) : # 모든 가장자리는 벽이므로 범위체크 필요 X
                nrx, nry, nbx, nby = rx, ry, bx, by

                while True :
                    nrx = nrx + dx[d]
                    nry = nry + dy[d]
                    if board[nrx][nry] == '#' : # 벽이면 뒤로한칸
                        nrx = nrx - dx[d]
                        nry = nry - dy[d]
                        break
                    if board[nrx][nry] == 'O' :
                        break

                while True :
                    nbx = nbx + dx[d]
                    nby = nby + dy[d]
                    if board[nbx][nby] == '#' :
                        nbx = nbx - dx[d]
                        nby = nby - dy[d]
                        break
                    if board[nbx][nby] == 'O' :
                        break
                        
                if board[nbx][nby] == 'O' : # 파란구슬이 구멍에 들어가면 안됨
                    continue
                    
                if nrx == nbx and nry == nby : # 동시에 같은칸에 있을 수 없음
                    if abs(nrx - rx) + abs(nry - ry) < abs(nbx - bx) + abs(nby - by) : # 두 구슬이 이동한 거리를 비교하여 더 많이 이동한 구슬을 한칸뒤로
                        nbx = nbx - dx[d]
                        nby = nby - dy[d]
                    else :
                        nrx = nrx - dx[d]
                        nry = nry - dy[d]

                if (nrx, nry, nbx, nby) not in visited :
                    q.append((nrx, nry, nbx, nby))

        cnt += 1
    print(-1)

bfs(rx, ry, bx, by)











