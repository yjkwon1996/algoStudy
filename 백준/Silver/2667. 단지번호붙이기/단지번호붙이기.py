# 단지번호붙이기. 1은 집이 있는 곳, 0은 집이 없는 곳. 좌우, 위아래로 다른 집과 연결됐으면 같은 단지
# 총 단지수와 각 단지내 집의 수를 오름차순 정렬해서 출력
# dfs?

import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1] # 상하좌우
dy = [-1, 1, 0, 0]

N = int(input()) # 지도의 크기(가로세로 N, 정사각형)
arr = [list(map(int, input().rstrip())) for _ in range(N)] # 지도

def dfs(x, y) :
    arr[x][y] = 0  # 이미 방문한 곳 중복 체크 방지

    for d in range(4) :
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or ny < 0 or nx >= N or ny >= N or arr[nx][ny] == 0:  # 지도 밖, 집이 없는 곳은 X
            continue
        global cnt
        cnt += 1 # 집의 개수를 추가
        dfs(nx, ny)

cnt = 1 # 단지 내 집의 수. 처음 시작하는 부분 포함 계산
house = [] # 단지 내 집의 수를 따로 저장해야함
answer = 0 # 총 단지 수

for i in range(N) :
    for j in range(N) :
        if arr[i][j] == 1 :
            dfs(i, j)
            house.append(cnt)
            answer += 1
            cnt = 1

house.sort() # 오름차순 정렬
print(answer)
for i in range(answer) :
    print(house[i])


