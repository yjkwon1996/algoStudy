# 왼쪽 위에서 오른쪽 아래로 이동. 항상 높이가 더 낮은 지점으로만 이동하면서
# 경로의 개수를 구하기
# 시간초과, dp?

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

M, N = map(int,input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(x, y) :

    # 목적지에 도착하면 1리턴 -> 이동한 모든 dp칸에 1만큼 추가
    if x == M-1 and y == N-1 :
        return 1

    # 탐색하지 않은 곳부터 탐색
    if dp[x][y] == -1 :
        dp[x][y] = 0 # 탐색 했는지 체크

        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]

            if 0<=nx<M and 0<=ny<N and arr[nx][ny] < arr[x][y] :
                dp[x][y] += dfs(nx, ny)

    # 이미 탐색한 곳이거나 탐색할 수 없는 곳이라면 종료.
    return dp[x][y]

print(dfs(0, 0))

