# 2048 (Easy).

import sys
input = sys.stdin.readline

# 위로 이동한 경우 -> 행부터 돌기
def up(arr) :
    tmpBoard = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N) :
        idx = 0
        pointValue = -1
        flag = False

        for j in range(N) :
            if arr[j][i] != 0 : # 블록이 있으면
                if flag : # 기준이 있는지 확인 후 있으면
                    if pointValue == arr[j][i] : # 두 값이 동일한지 확인 후 같으면
                        tmpBoard[idx][i] = pointValue*2 # 더한 값을 임시로 저장
                        pointValue = -1 # 이후 초기화
                        flag = False
                    else : # 두 값이 다르다면 갱신만
                        tmpBoard[idx][i] = pointValue
                        pointValue = arr[j][i]
                    idx += 1
                else : # 기준값이 없다면(빈칸)
                    pointValue = arr[j][i]
                    flag = True

        # 탐색 후 값이 남아있는 경우 tmp에 저장
        if pointValue != -1 :
            tmpBoard[idx][i] = pointValue

    return tmpBoard

# 아래로 이동 -> 행부터 돌기(끝에서부터 시작)
def down(arr) :
    tmpBoard = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N) :
        idx = N-1
        pointValue = -1
        flag = False

        for j in range(N-1, -1, -1) :
            if arr[j][i] != 0 : # 블록이 있으면
                if flag : # 기준이 있는지 확인 후 있으면
                    if pointValue == arr[j][i] : # 두 값이 동일한지 확인 후 같으면
                        tmpBoard[idx][i] = pointValue*2 # 더한 값을 임시로 저장
                        pointValue = -1 # 이후 초기화
                        flag = False
                    else : # 두 값이 다르다면 갱신만
                        tmpBoard[idx][i] = pointValue
                        pointValue = arr[j][i]
                    idx -= 1
                else : # 기준값이 없다면(빈칸)
                    pointValue = arr[j][i]
                    flag = True

        # 탐색 후 값이 남아있는 경우 tmp에 저장
        if pointValue != -1 :
            tmpBoard[idx][i] = pointValue

    return tmpBoard

# 좌로 이동 -> 열부터 돌기
def left(arr) :
    tmpBoard = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N) :
        idx = 0
        pointValue = -1
        flag = False

        for j in range(N) :
            if arr[i][j] != 0 : # 블록이 있으면
                if flag : # 기준이 있는지 확인 후 있으면
                    if pointValue == arr[i][j] : # 두 값이 동일한지 확인 후 같으면
                        tmpBoard[i][idx] = pointValue*2 # 더한 값을 임시로 저장
                        pointValue = -1 # 이후 초기화
                        flag = False
                    else : # 두 값이 다르다면 갱신만
                        tmpBoard[i][idx] = pointValue
                        pointValue = arr[i][j]
                    idx += 1
                else : # 기준값이 없다면(빈칸)
                    pointValue = arr[i][j]
                    flag = True

        # 탐색 후 값이 남아있는 경우 tmp에 저장
        if pointValue != -1 :
            tmpBoard[i][idx] = pointValue

    return tmpBoard

# 우로 이동 -> 열부터 돌기(끝에서부터 시작)
def right(arr) :
    tmpBoard = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N) :
        idx = N-1
        pointValue = -1
        flag = False

        for j in range(N-1, -1, -1) :
            if arr[i][j] != 0 : # 블록이 있으면
                if flag : # 기준이 있는지 확인 후 있으면
                    if pointValue == arr[i][j] : # 두 값이 동일한지 확인 후 같으면
                        tmpBoard[i][idx] = pointValue*2 # 더한 값을 임시로 저장
                        pointValue = -1 # 이후 초기화
                        flag = False
                    else : # 두 값이 다르다면 갱신만
                        tmpBoard[i][idx] = pointValue
                        pointValue = arr[i][j]
                    idx -= 1
                else : # 기준값이 없다면(빈칸)
                    pointValue = arr[i][j]
                    flag = True

        # 탐색 후 값이 남아있는 경우 tmp에 저장
        if pointValue != -1 :
            tmpBoard[i][idx] = pointValue

    return tmpBoard

def dfs(arr, num) :
    global answer
    if num == 5 : # 5번 수행하면 최댓값 찾기
        for i in range(N) :
            for j in range(N) :
                answer = max(answer, arr[i][j])

        return
    else : # 아니면 찾기
        tmp = up(arr)
        dfs(tmp, num + 1)
        tmp = down(arr)
        dfs(tmp, num + 1)
        tmp = left(arr)
        dfs(tmp, num + 1)
        tmp = right(arr)
        dfs(tmp, num + 1)

N = int(input().rstrip())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]
answer = 0

dfs(board, 0)
print(answer)




