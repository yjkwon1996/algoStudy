# 나이트의 이동. 체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다.
# 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?
#
#
#
# 입력
# 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
#
# 각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다.
# 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.
#
# 출력
# 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

import sys
from collections import deque
input = sys.stdin.readline

T = int(input().rstrip())
# knightMove = [[-2, -1], [-1, -2], [-2, 1], [-1, 2], [1, 2], [2, 1], [1, -2], [2, -1]]
dx = [-2, -1, -2, -1, 1, 2, 1, 2]
dy = [-1, -2, 1, 2, 2, 1, -2, -1]

def bfs() :
    global answer
    q = deque()
    q.append((cx, cy))
    visited[cx][cy] = 1 # 첫구간을 다시 방문할 필요 x

    while q :
        x, y = q.popleft()

        if x == targetX and y == targetY :
            print(visited[x][y]-1) # 첫 구간을 이미 간걸로 했었기 때문에 -1
            break

        for d in range(8) :
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < I and 0 <= ny < I and visited[nx][ny] == 0 :
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))



for _ in range(T) :
    I = int(input().rstrip()) # 체스판 한 변의 길이
    cx, cy = map(int, input().rstrip().split()) # 나이트가 현재 있는 칸
    targetX, targetY = map(int, input().rstrip().split()) # 나이트가 이동하려고 하는 칸
    visited = [[0 for _ in range(I)] for _ in range(I)]

    bfs()




