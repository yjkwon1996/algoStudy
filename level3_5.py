def solution(m, n, puddles):
    """
    m x n
    가장 왼쪽 위 집은 (1, 1). 학교는 가장 오른쪽 아래 (m, n)
    물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles,
    오른쪽과 아래쪽으로만 움직여 집에서 학교로 가는 최단경로의 개수를 1,000,000,007로 나눈 나머지
    """
    # m x n 2차원 배열 선언. 첫 윗줄과 왼쪽은 빈 칸으로 해서 (1,1)부터 시작
    arr = [[0 for col in range(m+1)] for row in range(n+1)]
    arr[1][1] = 1
    
    # puddles 지역은 0로
    for i, j in puddles :
        arr[j][i] = 0

    for i in range(1, n+1) :
        for j in range(1, m+1) :
            if i == 1 and j == 1 : continue
            if [j, i] not in puddles :
                arr[i][j] = arr[i-1][j] + arr[i][j-1]

    answer = arr[n][m] % 1000000007
    
    return answer

if __name__ == "__main__" :
    m, n = 4, 3
    puddles = [[2, 2]]
    # return = 4
    print(solution(m, n, puddles))
