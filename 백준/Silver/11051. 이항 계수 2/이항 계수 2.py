# 이항 계수2. 자연수
# \(N\)과 정수
# \(K\)가 주어졌을 때 이항 계수
# \(\binom{N}{K}\)를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에
# \(N\)과
# \(K\)가 주어진다. (1 ≤
# \(N\) ≤ 1,000, 0 ≤
# \(K\) ≤
# \(N\))
#
# 출력
#
# \(\binom{N}{K}\)를 10,007로 나눈 나머지를 출력한다.

import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

answer = 1
for i in range(K) :
    answer *= N
    N -= 1

div = 1
for i in range(2, K+1) :
    div *= i

print((answer // div) % 10007)






