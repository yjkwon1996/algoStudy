# 자연수 n이 주어졌을 때 n보다 크고 2n보다 작거나 같은 소수의 개수를 구하기

import sys
import math
innput = sys.stdin.readline

limit = 123456 # n의 최댓값

# 사전에 미리 소수를 찾아둬야 함
arr = [True for _ in range(2*limit + 1)] # True 면 소수
arr[0], arr[1] = False, False

# 에라토스테네스의 체 공식으로 소수를 미리 찾아두기
for i in range(2, int(math.sqrt(2*limit) + 1)) :
    if arr[i] :
        j = 2
        while i*j <= 2*limit :
            arr[i*j] = False
            j += 1

while True :
    n = int(input())

    if n == 0 : # 입력이 0인 경우 종료
        break

    cnt = 0
    # n부터, 2n 까지의 수 중에서 True인 수(소수)를 모두 찾아서 그 개수를 출력
    for i in range(n+1, 2*n + 1) :
        if arr[i] :
            cnt += 1
    print(cnt)

