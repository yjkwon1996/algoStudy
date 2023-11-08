# 뱀. 'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
# 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.
# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다.
# X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.


import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0] # 12 3 6 9시 방향
dy = [0, 1, 0, -1]

N = int(input().rstrip())
K = int(input().rstrip())

board = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K) :
    r, c = map(int, input().rstrip().split())
    board[r-1][c-1] = -1 # 사과가 있으면 -1로


time = 0
x, y = 0, 0 # 첫 시작 위치
dir = 1 # 처음에 오른쪽을 보는 상태에서 시작
q = deque() # 뱀의 몸 위치를 큐에다 저장
q.append((x, y)) # 처음엔 머리만

L = int(input().rstrip())
direction = []
for _ in range(L) :
    X, C = input().rstrip().split()
    direction.append((int(X), C))

idx = 0
while True :
    x = x + dx[dir]
    y = y + dy[dir]
    time += 1

    if 0>x or x>=N or 0>y or y>=N or (x, y) in q: # 벽이나 자기 몸에 박은경우
        break
    q.append((x, y)) # 이동

    # 이동 한 곳에 사과가 있다면
    if board[x][y] == -1 :
        # 사과를 먹고 몸을 길게
        board[x][y] = 0
    else : # 사과가 없다면, 꼬리를 한칸 줄여야함
        q.popleft()

    if time == direction[idx][0] : # X초동안 움직였으면 C방향으로 전환
        if direction[idx][1] == 'L' : # L은 왼쪽으로
            dir = (dir - 1) % 4
        else : # D는 오른쪽으로
            dir = (dir + 1) % 4

        if idx + 1 < len(direction) : # 다음 방향전환 수행
            idx += 1

        # 더이상 진행할 다음 방향전환이 없다면, 한쪽 방향으로 벽이나 자기 몸에 박을때까지 반복해서 간다.



print(time)













