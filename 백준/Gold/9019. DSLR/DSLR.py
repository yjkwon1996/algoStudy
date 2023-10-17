# DSLR. 4개의 명령어를 이용하는 간단한 계산기
# 각 명령어는 이 레지스터에 저장된 n을 다음과 같이 변환한다. n의 네 자릿수를 d1, d2, d3, d4라고 하자(즉 n = ((d1 × 10 + d2) × 10 + d3) × 10 + d4라고 하자)
#
# D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
# S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
# L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
# R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
# n = 1234 라면 여기에 L 을 적용하면 2341 이 되고 R 을 적용하면 4123

# bfs?


import sys
from collections import deque
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T) :
    A, B = map(int, input().rstrip().split())

    visited = [False for _ in range(10001)] # 이 숫자를 이전에 계산했다면 더 계산할 필요가 없으므로
    q = deque()

    # 시작
    q.append([A, ''])
    visited[A] = True

    while q :
        number, order = q.popleft()

        if number == B : # A가 B가 됐다면 끝
            print(order)
            break

        # DSLR 각각의 경우를 큐에 넣는다.
        D = 2 * number % 10000 # 10000넘으면 나머지
        if not visited[D] :
            visited[D] = True
            q.append([D, order + 'D'])

        S = (number-1) % 10000 # n이 0이면 9999를 레지스터에 저장
        if not visited[S] :
            visited[S] = True
            q.append([S, order + 'S'])

        # 각 자릿수를 왼편으로 회전
        L = (number % 1000)*10 + (number // 1000) # 1234 -> 2341.
        if not visited[L] :
            visited[L] = True
            q.append([L, order + 'L'])

        # 각 자릿수를 오른편으로 회전
        R = (number % 10) * 1000 + (number // 10)  # 1234 -> 4123.
        if not visited[R]:
            visited[R] = True
            q.append([R, order + 'R'])





