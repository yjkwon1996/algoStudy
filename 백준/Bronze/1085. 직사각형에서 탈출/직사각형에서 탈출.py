# 직사각형에서 탈출.
# 현재 (x, y)좌표에 있고 왼쪽 아래 (0, 0)이고 오른쪽 위는 (w, h)일 때
# 직사각형의 경계선까지 가는 거리의 최솟값

import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().rstrip().split())

# x좌표와 0과 w비교, y좌표와 0과 h를 비교해서 가장 가까운 쪽의 거리
print(min(x, w-x, y, h-y))