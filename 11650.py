# 11650 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

"""
2차원 평면 위의 점 N개가 주어진다.
좌표를 x가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램 작성
"""
# 첫째 줄에 점의 개수 N(1 <= N <= 100000)이 주어진다.
# 두 번째 줄부터 N개의 줄에는 i번 점의 위치 xi, yi가 주어진다. (-100000 <= xi, yi <= 100000)
# 좌표는 항상 정수이고 위치가 같은 두 점은 없다.

# x 좌표 순으로 정렬한 뒤, 그 내부에서 y좌표 순으로 정렬

N = int(input())

point = []

for _ in range(N) :
    x, y = map(int, input().split())
    point.append([x, y])

point.sort()

for i in range(N) :
    print(point[i][0], point[i][1])

