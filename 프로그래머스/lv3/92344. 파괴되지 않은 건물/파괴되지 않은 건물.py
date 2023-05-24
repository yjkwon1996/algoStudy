def solution(board, skill):
    answer = 0
    # skill : [type, r1, c1, r2, c2, degree]
    # type : 1 공격, 2 회복. r1, c1, r2, c2, degree -> 범위 내에 내구도를 degree만큼 조정
    row = len(board)
    col = len(board[0])
    arr = [[0 for _ in range(col+1)] for _ in range(row+1)]
    
    for type, r1, c1, r2, c2, degree in skill :
        # 1은 공격(board 값 감소), 2는 회복(board 값 증가)
        if type == 1 :
            type = -1
        else : 
            type = 1
            
        # 각 끝점을 표시. 끝나는 부분에는 -를 적용시켜 그 범위에만 적용되도록함
        arr[r1][c1] += degree * type
        arr[r1][c2+1] -= degree * type
        arr[r2+1][c1] -= degree * type
        arr[r2+1][c2+1] += degree * type
    
    # 누적합 계산(가로)
    for i in range(row) :
        for j in range(1, col) :
            arr[i][j] += arr[i][j-1]
    
    # 누적합(세로)
    for i in range(1, row) :
        for j in range(col) :
            arr[i][j] += arr[i-1][j]
    
    for i in range(row) :
        for j in range(col) :
            board[i][j] += arr[i][j]
            if board[i][j] > 0 :
                answer += 1
                
    return answer