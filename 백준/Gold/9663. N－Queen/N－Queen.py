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