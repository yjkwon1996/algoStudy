# -*- coding: utf-8 -*-
# 9663 N-Queen
# https://www.acmicpc.net/problem/9663

"""
N-Queen 문제는 크기가 N x N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램 작성
"""
# 입력 : 첫째 줄에 N(1<= N <= 15)
# 출력 : 첫째 줄에 N개를 서로 공격할 수 없게 놓는 경우의 수

# 같은 행, 같은 열, 같은 대각선 상에 2개 이상의 퀸이 존재하면 안된다
# col[i], col[k] : i, k번째 행에서 퀸이 놓여있는 열의 위치
# col[i] == col[k] : 같은 열에 2개의 퀸이 존재한다 - 실패
# col[i] - col[k] == i - k or k - i 대각선 상에 퀸이 존재 - 실패
# col 각 값의 idx가 행을 의미하고, 값은 열을 의미한다.
# col[i] = j -> [i, j] 위치에 퀸이 존재한다 or 두겠다.

"""
# 시간초과 발생

N = int(input())
col = [0] * (N+1)
answer = 0

def check(i, col) :
    k = 1
    flag = True # 대각선상에 없다면 True, 있다면 False로 대각선상에 2개 이상의 퀸이 존재한다면 조건에 만족x
    while (k < i and flag) : # i보다 작은 모든 k에 대해서 확인함으로써 이전에 두었던 퀸과 비교를 해서
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)) : # 같은 열에 있거나 대각선상에 있다면
            flag = False
        k += 1  # i이하의 모든 k에 대해서(i 이전의 행에 두어진 퀸과 비교)
    return flag

def nqueen(i, col) :
    global answer
    n = len(col) - 1
    if (check(i, col)) : # N개의 퀸이 서로 공격할 수 없는 조건을 만족하면서
        if (i == n) : # 끝까지 탐색하며 체스판 위에 N개의 퀸을 놓았다면
            # print(col[1:n+1])
            answer += 1
        else :  # 탐색을 덜 했다면, 
            for j in range(1, n+1) : 
                col[i+1] = j # 다음행 j열에 퀸을 놓고 백트래킹(다음 행의 모든 열에 퀸을 두고 가능한지 계산)
                nqueen(i+1, col)

nqueen(0, col)
print(answer)

"""
import sys

N = int(sys.stdin.readline())
col = [0] * (N)
answer = 0

def check(x) :
    for i in range(x) : # 입력받은 x행 위쪽의 모든 행에 존재하는 퀸들과 비교하여
        if col[x] == col[i] or abs(col[x] - col[i]) == x - i : # 같은 열에 있거나 대각선상에 퀸이 2개 이상 있다면
            return False
    return True # 같은 열, 행, 대각선상에 퀸이 2개 이상 없으므로 퀸을 둘 수 있는 자리가 된다.

def nqueen(x) :
    global answer
    # N개의 퀸이 서로 공격할 수 없는 조건을 만족하면서
    # 끝까지 탐색하며 체스판 위에 N개의 퀸을 놓았다면
    if x == N : 
        # print(col[1:n+1])
        answer += 1
        
    else :  # 탐색을 덜 했다면, 
        for i in range(N) : # x행의 모든 열을 탐색
            col[x] = i # x행 i열에 퀸을 놓고 백트래킹
            if check(x) : # 퀸을 둘 수 있다면 다음 행으로 넘어가서 백트래킹
                nqueen(x+1)

nqueen(0) # 0행부터 시작, N행까지
print(answer)

# 시간초과 너무 어렵다고함?

