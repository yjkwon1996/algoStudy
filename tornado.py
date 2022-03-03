# 마법사 상어와 토네이도
# https://www.acmicpc.net/problem/20057

# 토네이도를 크기가 N X N인 격자로 나누어진 모래밭에서 연습. 
# 위치(r, c)는 격자의 r행 c열, A[r][c]는 (r, c)에 있는 모래의 양
# 토네이도를 시전하면 격자의 가운데 칸부터 토네이도의 이동이 시작. 토네이도는 한 번에 한 칸 이동
# 토네이도가 이동할 때마다 모래는 일정한 비율로 흩날리게 된다.
# 토네이도는 (1, 1)까지 이동한 뒤 소멸. 모래가 격자의 바깥으로 이동 가능
# 토네이도가 소멸되었을 때 격자의 바깥으로 나간 모래의 양을 구하라.
# 토네이도는 한 방향으로 이동하는 거리는 방향을 바꿀 때마다 1 증가
# 방향이 바뀌는 것은 반시계 방향으로 90

# 모래 양 계산
def sand_value(time, dx, dy, direction):
    global ans, sandx, sandy

    # y좌표 계산 & x좌표 갱신
    for _ in range(time):
        sandx += dx
        sandy += dy
        if sandy < 0:  # 토네이도 위치가 범위 밖이면 stop
            break

        # ans, out_sand
        total = 0  # 이동하는 모래양
        for dx, dy, z in direction:
            nx = sandx + dx
            ny = sandy + dy
            if z == 0:  # ans (나머지)
                new_sand = sand[sandx][sandy] - total
            else:  # 비율
                new_sand = int(sand[sandx][sandy] * z)
                total += new_sand

            if 0 <= nx < N and 0 <= ny < N:   # 인덱스 범위이면 값 갱신
                sand[nx][ny] += new_sand
            else:  # 범위 밖이면 ans에 밖으로 나간 모래를 추가해준다.
                ans += new_sand


N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]

# 방향별 모래 비율 위치.(x좌표, y좌표, 모래 비율)
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]

sandx, sandy = N//2, N//2  # 시작좌표
ans = 0  # out_sand

# 토네이도 회전 방향
for i in range(1, N + 1):
    if i % 2:
        sand_value(i, 0, -1, left)
        print(ans, sandx, sandy)
        sand_value(i, 1, 0, down)
        print(ans, sandx, sandy)
    else:
        sand_value(i, 0, 1, right)
        print(ans, sandx, sandy)
        sand_value(i, -1, 0, up)
        print(ans, sandx, sandy)

print(ans)




"""
5
0 0 0 0 0
0 0 0 0 0
0 10 0 0 0
0 0 0 0 0
0 0 0 0 0

10
------------------------
5
0 0 0 0 0
0 0 0 0 0
0 100 0 0 0
0 0 0 0 0
0 0 0 0 0

85
------------------------
7
1 2 3 4 5 6 7
1 2 3 4 5 6 7
1 2 3 4 5 6 7
1 2 3 0 5 6 7
1 2 3 4 5 6 7
1 2 3 4 5 6 7
1 2 3 4 5 6 7

139
------------------------
5
100 200 300 400 200
300 243 432 334 555
999 111 0 999 333
888 777 222 333 900
100 200 300 400 500

7501
------------------------
5
0 0 100 0 0
0 0 100 0 0
0 0 0 0 0
0 0 100 0 0
0 0 100 0 0

283
------------------------
9
193 483 223 482 858 274 847 283 748
484 273 585 868 271 444 584 293 858
828 384 382 818 347 858 293 999 727
818 384 727 373 636 141 234 589 991
913 564 555 827 0 999 123 123 123
321 321 321 983 982 981 983 980 990
908 105 270 173 147 148 850 992 113
943 923 982 981 223 131 222 913 562
752 572 719 590 551 179 141 137 731

22961
"""