
board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]

"""
1과 0으로 채워진 2차원 배열 board
표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return
가로와 세로가 모두 1

0 1 1 1 0 1 1 1 1
0 1 1 0 1 1 1 1 1
1 1 1 0 0 1 1 1 1
1 0 0 1 1 1 1 1 1
0 0 0 0 1 1 1 1 1
0 1 0 0 0 0 0 0 1
1 0 1 0 1 0 1 0 1
0 0 0 0 0 0 0 0 0
1 0 0 1 1 0 0 0 0

진행하면서 1을 발견하면 왼쪽, 위쪽, 왼쪽 위 세 방향을 확인했을때 모두 1이면 정사각형
-> 2(가로, 세로가 2칸인 정사각형)
반복한다면, 가로세로가 3, 4인 정사각형도 계산이 가능
board의 값에서 반복하면서 값을 변경해내는 것을 끝내면
가로 * 세로의 크기를 return
"""
answer = 0

row = len(board)
column = len(board[0])

size = []
count = 0
for y in range(1, row) :       
    for x in range(1, column) :
        if board[y][x] == 1 :
            board[y][x] = min(board[y-1][x-1], board[y-1][x], board[y][x-1]) + 1
            
for i in range(row) :
    answer = max(answer, max(board[i]))

end = answer * answer