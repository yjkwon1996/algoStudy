# 분산처리
# 10대의 컴퓨터로 작업한다면 마지막 데이터가 처리될 컴퓨터의 번호는?

# # 시간초과
# import sys
# input = sys.stdin.readline
#
# T = int(input().rstrip())
#
# for _ in range(T) :
#     a, b = map(int, input().rstrip().split()) # 데이터의 갯수는 a^b
#     print((a ** b) % 10) # 10대의 컴퓨터로 분산처리하고 나머지

# 각 수를 승수만큼 곱해서 10으로 나눈 것의 1의 자리만 출력하면 됨
# 각 숫자를 제곱했을 때의 끝자리 수들은
# 0 - 10 / 1 - 1 / 2 - 2 4 6 8 / 3 - 9 7 1 / 4 - 4 6
# 5 - 5 / 6 - 6 / 7 - 9 3 1 / 8 - 8 4 2 6 / 9 - 9 1

import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T) :
    a, b = map(int, input().rstrip().split()) # 데이터의 갯수는 a^b
    a = a % 10

    if a == 0 :
        print(10)
    elif a == 1 or a == 5 or a == 6 :
        print(a)
    elif a == 4 or a == 9 :
        if b % 2 == 0 :
            print((a*a) % 10)
        else :
            print(a)
    else :
        if b % 4 == 0 :
            print((a**4) % 10)
        else :
            print((a**b) % 10)




