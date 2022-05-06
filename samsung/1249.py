# -*- coding: utf-8 -*-
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV15QRX6APsCFAYD&categoryId=AV15QRX6APsCFAYD&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1
# 1249. [S/W 문제해결 응용] 4일차 - 보급로

# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input()) # 지도의 크기 N x N
    
    arr = [list(map(int, input())) for _ in range(N)]
    
    # (0, 0)에서 시작해서 (N-1, N-1)에 도착
    # bfs
    # (0,0)에서 시작해서 각 배열 위치까지마다 걸리는 시간을 누적하는 방식으로
    time = [[90000] * N for _ in range(N)] # 한칸당 걸리는 최대시간은 9, 최대크기는 100*100 -> 90000이 최대값
    time[0][0] = 0 # 시작점은 0
    
    q = deque()
    q.append((0, 0))
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    while q :
        # q에서 좌표를 꺼내서
        x, y = q.popleft()
        
        # 다음 좌표를 계산
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
        
            # 각각 다음 좌표로 이동이 가능하다면
            if 0 <= nx < N and 0 <= ny < N :
                # 거리를 비교해서 더 빠른 길이라면 값을 갱신하고 좌표를 추가
                if time[x][y] + arr[nx][ny] < time[nx][ny] :
                    time[nx][ny] = time[x][y] + arr[nx][ny]
                    q.append((nx, ny))
                    
    # 이후 걸리는 시간을 계산한 리스트의 마지막 좌표만 출력하면 최단시간이 출력된다.
    print("#{} {}".format(test_case, time[N-1][N-1])) 


