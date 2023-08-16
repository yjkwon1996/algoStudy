# 어떤 지역의 높이 정보가 주어졌을 때 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산
# 행, 열의 개수 N

import sys
import copy
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N = int(input())
originArr = [list(map(int, input().rstrip().split())) for _ in range(N)]
originVisited = [[False for _ in range(N)] for _ in range(N)]

# 비의 양을 하나씩 조절하면서 물에 잠기지 않는 영역이 최대가 되는 경우 찾기
# 최소값부터 최대값까지?
mini = min(map(min, originArr))
maxi = max(map(max, originArr))
answer = 1
for i in range(mini, maxi) :
    arr = copy.deepcopy(originArr)
    visited = copy.deepcopy(originVisited)
    q = deque()
    ans = 0

    for j in range(N) :
        for k in range(N) :
            arr[j][k] -= i

    for j in range(N) :
        for k in range(N) :
            if 1 <= arr[j][k] <= 100 and not visited[j][k]:
                q.append([j, k])

                while q :
                    x, y = q.popleft()

                    for d in range(4) :
                        nx = x+dx[d]
                        ny = y+dy[d]

                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] > 0 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append([nx, ny])

                ans += 1

    if ans > answer :
        answer = ans

print(answer)

