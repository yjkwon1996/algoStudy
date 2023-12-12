# 수들의 합. 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?
#
# 입력
# 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.
#
# 출력
# 첫째 줄에 자연수 N의 최댓값을 출력한다.

import sys
input = sys.stdin.readline

S = int(input().rstrip())

# 1부터 시작해서 합이 S

N = 1
su = 0

while True :
    su += N
    if su > S :
        print(N-1)
        break

    N += 1








