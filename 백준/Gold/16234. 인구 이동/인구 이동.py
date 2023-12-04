# 인구 이동. N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다.
# 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.
# 오늘부터 인구 이동이 시작되는 날이다.
# 인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.
# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.
# 각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.

# 첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)
# 둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)
# 인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.

# 인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, L, R = map(int, input().rstrip().split())
A = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]


answer = 0

# dfs로 하나의 연합을 모두 합하고 나중에 정리
# 연합의 국가 각각의 위치만 기억하고
result = []
def dfs(x, y) :
    for d in range(4) :
        nx = x + dx[d]
        ny = y + dy[d]

        if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and L<=abs(A[nx][ny] - A[x][y])<=R :
            visited[nx][ny] = True
            result.append((nx, ny))
            dfs(nx, ny)

while True :
    visited = [[False for _ in range(N)] for _ in range(N)]
    flag = False

    for i in range(N) :
        for j in range(N) :
            result = []

            if not visited[i][j] :
                result.append((i, j))
                visited[i][j] = True
                dfs(i, j)

                if len(result) == 1 : # 연합이 없는 경우
                    continue

                # 연합이 있는 경우
                flag = True
                avg = sum(A[x][y] for x, y in result) // len(result)
                for x, y in result :
                    A[x][y] = avg

    if not flag : # 모두 탐색했는데 연합이 아무것도 없다면 종료
        break

    answer += 1


print(answer)







