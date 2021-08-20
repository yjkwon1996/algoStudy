

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]] # answer = 2


"""
컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers
연결되어 있는 경우 같은 네트워크
네트워크의 개수를 return
computer[i][i]는 항상 1, computer[i][j] = computer[j][i], 연결되면 1
연결되어 있는 네트워크와 연결되지 않은 네트워크를 구분
연결되어 있는 경우 배열에서 pop
"""
answer = 0
arr = []
visit = [0] * n

while 0 in visit :
    arr.append(visit.index(0))
    while arr :
        node = arr.pop(0)
        visit[node] = 1
        for i in range(n) :
            if visit[i] == 0 and computers[node][i] == 1 :
                arr.append(i)
    answer += 1
