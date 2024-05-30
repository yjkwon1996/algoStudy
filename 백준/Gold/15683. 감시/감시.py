# 감시. 15683

import sys
import copy
input = sys.stdin.readline

dy = [-1, 0, 1, 0] # 상 우 하 좌
dx = [0, 1, 0, -1]

directions = { 1 : [[0], [1], [2], [3]], # 1번 cctv는 상하좌우 한 방향으로
               2 : [[0, 2], [1, 3]], # 2번 cctv는 상하 or 좌우
               3 : [[0, 1], [1, 2], [2, 3], [3, 0]], # 3번 cctv
               4 : [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], # 4번 cctv
               5 : [[0, 1, 2, 3]] } # 5번 cctv

N, M = map(int, input().rstrip().split())
arr = []
cctv = []

for i in range(N) :
    value = list(map(int, input().rstrip().split()))
    arr.append(value)
    for j in range(M) :
        if value[j] in [1, 2, 3, 4, 5] :
            cctv.append([value[j], i, j])

def check(arr, dir, x, y) :
    for d in dir :
        nx = x
        ny = y
        while True :
            nx += dx[d]
            ny += dy[d]
            # if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0 :
            #     arr[nx][ny] = -1

            if nx < 0 or nx >= N or ny < 0 or ny >= M :
                break
            if arr[nx][ny] == 6 :
                break
            elif arr[nx][ny] == 0 :
                arr[nx][ny] = -1


def dfs(arr, depth) :
    global answer

    if depth == len(cctv) :
        cnt = 0
        for i in range(N) : # 사각지대 찾기
            cnt += arr[i].count(0)

        answer = min(answer, cnt)
        return

    tmp = copy.deepcopy(arr)
    cctvNum, x, y = cctv[depth]
    for dir in directions[cctvNum] :
        check(tmp, dir, x, y)
        dfs(tmp, depth+1)
        tmp = copy.deepcopy(arr)

answer = sys.maxsize
dfs(arr, 0)
print(answer)
