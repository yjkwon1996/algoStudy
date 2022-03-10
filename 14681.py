# 14681 사분면 고르기
# https://www.acmicpc.net/problem/14681

# 주어진 점이 어느 사분면에 속하는지 알아내는 것
# (x, y) - 1, (-x, y) - 2, (-x, -y) - 3, (x, -y) - 4
# 점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램

# 첫 줄에는 정수 x, 다음 줄에는 정수 y 입력

x = int(input())
y = int(input())

if x > 0 and y > 0 :
    print("1")
elif x < 0 and y > 0 :
    print("2")
elif x < 0 and y < 0 :
    print("3")
else :
    print("4")

