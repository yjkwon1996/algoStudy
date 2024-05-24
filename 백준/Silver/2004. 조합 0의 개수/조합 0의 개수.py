# 조합 0의 개수.  
# $n \choose m$의 끝자리
# $0$의 개수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수
# $n$,
# $m$ (
# $0 \le m \le n \le 2,000,000,000$,
# $n \ne 0$)이 들어온다.
#
# 출력
# 첫째 줄에
# $n \choose m$의 끝자리
# $0$의 개수를 출력한다.

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

# 끝자리가 0 -> 2와 5의 곱
# 2 5의 쌍을 구하면 0의 갯수를 구하기 가능

def two(n) :
    value = 0
    while n != 0 :
        n = n // 2
        value += n
    return value

def five(n) :
    value = 0
    while n != 0:
        n = n // 5
        value += n
    return value

answer = min(two(n) - two(m) - two(n-m), five(n) - five(m) - five(n-m))

print(answer)


