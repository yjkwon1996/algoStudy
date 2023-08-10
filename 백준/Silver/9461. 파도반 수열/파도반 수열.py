# 나선 모양의 삼각형. P(N)은 나선에 있는 삼각형의 변의 길이. N이 주어졌을 때 P(N)을 구하기
# ex) P(10) -> 1 1 1 2 2 3 4 5 7 9 -> P(N) = P(N-3) + P(N-2)

import sys
input = sys.stdin.readline

T = int(input())

P = [0 for _ in range(100)] # 1 <= N <= 100
P[0] = 1
P[1] = 1
P[2] = 1

for i in range(3, 100):
    P[i] = P[i - 3] + P[i - 2]

for _ in range(T) :
    N = int(input())
    print(P[N-1]) # P[0]부터 채웠으므로 -1

