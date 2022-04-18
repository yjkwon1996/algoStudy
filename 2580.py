# -*- coding: utf-8 -*-
# 2580 스도쿠
# https://www.acmicpc.net/problem/2580

"""
스도쿠는 18세기 스위스 수학자가 만든 '라틴 사각형'이랑 퍼즐에서 유래한 것으로 현재 많은 인기를 누리고 있다.
이 게임은 아래 그림과 같이 가로, 세로 각각 9개씩 총 81개의 작은 칸으로 이루어진 정사각형 판 위에서 이뤄진다.
게임 시작 전 일부 칸에는 1부터 9까지의 숫자 중 하나가 쓰여 있다
나머지 빈 칸을 채우는 방식은 각각의 가로줄과 세로줄에는 1 ~ 9의 숫자가 각각 하나씩만 등장
굵은 선으로 구분된 3x3 정사각형 안에도 1 ~ 9의 숫자가 각각 하나씩만 등장
"""
# 입력 : 아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판 각 줄에 쓰여 있는 숫자가 한 칸씩 띄워서 차례로 주어짐
# 빈 칸의 경우 0이 주어지고 규칙대로 채울수 없는 경우는 없다.
# 출력 : 모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉 줄에 걸쳐 한 줄에 9개씩 한 칸씩 띄워서 출력
# 스도쿠 판을 채우는 방법이 여러가지인 경우 그 중 하나만 출력


# 시간초과
import sys

arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]

# 0이 있는 위치를 저장(빈칸 찾기)
zero_point = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]

# print(arr)
# print(zero_point)


# 0이 있는 위치에서, 가로 세로 탐색 후 1~9 중 들어갈 수 있는 수 찾기
# 3x3의 범위에서도 탐색해야함



def find_number(i, j) : 
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for k in range(9) :
        if arr[i][k] in num : # 가로 범위로 탐색하면서 1~9 중 없는 숫자(빈칸에 넣을 수 있는 숫자) 찾기
            num.remove(arr[i][k])
        if arr[k][j] in num : # 세로 범위로 탐색하면서 1~9 중 없는 숫자(빈칸에 넣을 수 있는 숫자) 찾기
            num.remove(arr[k][j]) 
    
    # 3x3
    i = i//3
    j = j//3
    
    for x in range(i*3, (i+1)*3) : # 가로 3
        for y in range(j*3, (j+1)*3) : # 세로 3
            if arr[x][y] in num : # 3x3 범위로 탐색하면서 1~9 중 없는 숫자(빈칸에 넣을 수 있는 숫자) 찾기
                num.remove(arr[x][y])
                
    return num # 빈칸에 들어갈 수 있는 숫자를 찾아서 리턴

flag = False # 모든 빈칸을 다 채웠는지 확인용
def sudoku(point) :
    global flag
    
    if flag == True : # 백트래킹 중에 모든 빈칸을 다 채웠다면
        return
    
    if point == len(zero_point) : # 모든 0을 채웠다면
        for i in arr:
            print(*i)
        flag = True
        return
    else : # 다 못채웠다면 채우러 백트래킹
        (i, j) = zero_point[point]
        promising = find_number(i, j) # 빈 칸에 가능한 숫자의 배열
        
        for x in promising :
            arr[i][j] = x # 가능한 숫자 중 하나를 넣어주고
            sudoku(point+1) # 다음 빈칸을 찾아서
            arr[i][j] = 0 # 이번 조합으로 빈칸을 모두 채울 수 없다면 0으로 초기화
            
sudoku(0)
    





"""
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
"""