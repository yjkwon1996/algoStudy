# 골드바흐의 추측. 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
# 8 = 3 + 5, 3과 5는 모두 홀수인 소수. 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23
# 백만 이하의 모든 짝수에 대하여 이 추측을 검증하라.
# n = a + b 형태로 출력. a와 b는 홀수 소수, n을 만들 수 있는 방법이 여러가지라면 b-a가 가장 큰 것을 출력

import sys
input = sys.stdin.readline

# 소수 판별을 위한
limit = 1000001
arr = [1 for _ in range(limit)]
for i in range(3, int(limit**0.5)+1, 2) : # 제곱근까지만, 홀수만
    if arr[i] == 1:
        for j in range(i*2, limit, i) :
            arr[j] = 0


while True :
    n = int(input().rstrip())
    if n == 0 : # 입력의 마지막
        break

    for i in range(3, int(n/2)+1, 2) : # i를 작은 수에서부터 시작.
        if arr[i] == 1 and arr[n-i] :
            print("%d = %d + %d" % (n, i, n-i))
            break
    else : # 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우
        print("Goldbach's conjecture is wrong.")


