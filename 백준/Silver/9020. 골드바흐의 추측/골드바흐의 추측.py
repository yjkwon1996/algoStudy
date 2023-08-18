# 골드바흐 수 : 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다.
# 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.
# 짝수 n이 주어지면 n의 골드바흐 파티션을 출력

import sys
input = sys.stdin.readline

T = int(input())

def prime(x) :
    if x == 1 :
        return False
    for i in range(2, int(x**0.5)+1) : # x가 sqrt(x) 이하의 수로 나누어 떨어지지 않으면 그 이상의 수는 볼 필요 없음
        if x % i == 0 :
            return False
    return True

for _ in range(T) :
    n = int(input().rstrip())
    a, b = n//2, n//2 # 반으로 쪼개서 하나씩 확인

    while a > 0 :
        if prime(a) and prime(b) : # 두 수가 모두 소수면 출력
            print(a, b)
            break
        else :
            a -= 1
            b += 1


