# 1x1 정사각형 4개를 이어서 붙인 도형이 테트로미노
# N x M 종이 위에 테트로미노 하나를 적절하게 놓아서 수의 합을 최대로 하기

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

answer = 0

# 모든 방향으로 4번까지 이동하기 - ㅗ, ㅜ, ㅓ, ㅏ 모양을 제외한 경우만 탐색이 됐음 -> 따로 탐색
def dfs(x, y, depth, valueSum) :
    global answer
    if depth == 4 : # 4번 이동했으면 최댓값과 비교
        answer = max(answer, valueSum)
        return

    # 아직 4번 이동하지 않았다면, 이동 가능한 다음 공간을 찾아서 이동
    for d in range(4) :
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny] :
            visited[nx][ny] = True
            dfs(nx, ny, depth+1, valueSum+arr[nx][ny])
            visited[nx][ny] = False

# ㅗ, ㅜ, ㅓ, ㅏ 모양은 위 dfs로 탐색할 수 없으므로 별도로 찾아줘야 한다.
def dfs2(x, y) :
    global answer
    for i in range(4) : # ㅗ, ㅜ, ㅓ, ㅏ 4개
        s = arr[x][y] # 초기값
        for j in range(3) : # 3방향만을 쓰기 위해 계산
            d = (i+j)%4
            nx = x + dx[d]
            ny = y + dy[d]

            if not ( 0<=nx<N and 0<=ny<M) : # 범위 밖으로 나가면 안됨
                s = 0 # 초기값은 초기화
                break
            s += arr[nx][ny]
        answer = max(answer, s)

for i in range(N) :
    for j in range(M) :
        visited[i][j] = True
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = False
        dfs2(i, j)

print(answer)