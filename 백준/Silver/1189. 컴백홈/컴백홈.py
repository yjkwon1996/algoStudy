# 컴백홈. 한수는 캠프를 마치고 집에 돌아가려 한다. 한수는 현재 왼쪽 아래점에 있고 집은 오른쪽 위에 있다. 그리고 한수는 집에 돌아가는 방법이 다양하다.
# 단, 한수는 똑똑하여 한번 지나친 곳을 다시 방문하지는 않는다.
#
#       cdef  ...f  ..ef  ..gh  cdeh  cdej  ...f
#       bT..  .T.e  .Td.  .Tfe  bTfg  bTfi  .Tde
#       a...  abcd  abc.  abcd  a...  a.gh  abc.
# 거리 :  6     6     6     8     8    10    6
# 위 예제는 한수가 집에 돌아갈 수 있는 모든 경우를 나타낸 것이다. T로 표시된 부분은 가지 못하는 부분이다.
# 문제는 R x C 맵에 못가는 부분이 주어지고 거리 K가 주어지면 한수가 집까지도 도착하는 경우 중 거리가 K인 가짓수를 구하는 것이다.
#
# 입력
# 첫 줄에 정수 R(1 ≤ R ≤ 5), C(1 ≤ C ≤ 5), K(1 ≤ K ≤ R×C)가 공백으로 구분되어 주어진다. 두 번째부터 R+1번째 줄까지는 R×C 맵의 정보를 나타내는 '.'과 'T'로 구성된 길이가 C인 문자열이 주어진다.
#
# 출력
# 첫 줄에 거리가 K인 가짓수를 출력한다.

import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

R, C, K = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

def dfs(x, y, depth) :
    global answer

    if depth == K : # K거리를 돌았는데
        if x == 0 and y == C-1 : # 목적지에 도착한 경우면
            answer += 1

        return # 도착 안했으면 그냥 끝

    # K 거리를 아직 덜 돌았으므로 더 돌아야됨
    for d in range(4) :
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != 'T' and not visited[nx][ny] :
            visited[nx][ny] = True
            dfs(nx, ny, depth+1)
            visited[nx][ny] = False


answer = 0
visited[R-1][0] = True
dfs(R-1, 0, 1) # 왼쪽 아래 시작

print(answer)





