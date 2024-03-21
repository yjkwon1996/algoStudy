# 불!. 지훈이는 미로에서 일을 한다. 지훈이를 미로에서 탈출하도록 도와주자!
#
# 미로에서의 지훈이의 위치와 불이 붙은 위치를 감안해서 지훈이가 불에 타기전에 탈출할 수 있는지의 여부, 그리고 얼마나 빨리 탈출할 수 있는지를 결정해야한다.
#
# 지훈이와 불은 매 분마다 한칸씩 수평또는 수직으로(비스듬하게 이동하지 않는다) 이동한다.
#
# 불은 각 지점에서 네 방향으로 확산된다.
#
# 지훈이는 미로의 가장자리에 접한 공간에서 탈출할 수 있다.
#
# 지훈이와 불은 벽이 있는 공간은 통과하지 못한다.
#
# 입력
# 입력의 첫째 줄에는 공백으로 구분된 두 정수 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1000 이다. R은 미로 행의 개수, C는 열의 개수이다.
#
# 다음 입력으로 R줄동안 각각의 미로 행이 주어진다.
#
# 각각의 문자들은 다음을 뜻한다.
#
# #: 벽
# .: 지나갈 수 있는 공간
# J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# F: 불이 난 공간
# J는 입력에서 하나만 주어진다.
#
# 출력
# 지훈이가 불이 도달하기 전에 미로를 탈출 할 수 없는 경우 IMPOSSIBLE 을 출력한다.
#
# 지훈이가 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간을 출력한다.

import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

R, C = map(int, input().rstrip().split())
arr = []

now = []
fire = [] # 불은 여러곳에서 발생 가능!!!
for i in range(R) :
    tmp = list(input().rstrip())
    for j in range(C) :
        if tmp[j] == 'J' :
            now = [i, j]
        elif tmp[j] == 'F' :
            fire.append([i, j])
    arr.append(tmp)

def bfs() :
    q = deque()
    q.append((now[0], now[1], 'J')) # 사람 따로
    arr[now[0]][now[1]] = 0 # 방문 체크 대신 거리로


    for x, y in fire : # 불 따로
        q.append((x, y, 'F'))
        arr[x][y] = '#'

    while q :
        x, y, o = q.popleft()
        if o == 'J' and ( x == 0 or y == 0 or x == R-1 or y == C-1 ) : # 모서리에 도달했는데
            if arr[x][y] == '#' : # 벽이면 못나감
                continue
            return arr[x][y] + 1 # 벽이 아니면 나감

        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < R and 0 <= ny < C : # 범위 내에서
                if o == 'J' and arr[nx][ny] == '.' and arr[x][y] != '#' : # 사람이 갈 수 있는 경우(불이랑 동시 진행이므로 현재 공간도 확인해야함)
                    arr[nx][ny] = arr[x][y] +1 # J에서 진행하던 현재 공간이 불타는 경우가 있음.
                    q.append((nx, ny, 'J'))
                elif o == 'F' and arr[nx][ny] != '#' :
                    arr[nx][ny] = '#'
                    q.append((nx, ny, 'F'))

    return "IMPOSSIBLE" # 탈출구를 찾지 못한 경우

answer = bfs()
print(answer)










