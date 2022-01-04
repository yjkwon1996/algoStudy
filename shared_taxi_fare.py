# 2021 KAKAO BLIND RECRUITMENT
# 합승 택시 요금
# https://programmers.co.kr/learn/courses/30/lessons/72413

# 정확성과 효율성 테스트가 있음
# 최단 경로 탐색 알고리즘
# 최단 경로를 탐색하되, 특정 지점을 반드시 방문해야함
# 지점의 개수 n, 출발지점 s, A의 도착지점 a, B의 도착지점 b, 지점 사이의 예상 택시요금 fares
# s에서 출발해서 a와 b에 도착해야 한다.
# 합승을 하지않고 따로 이동하는 경우의 예상 택시요금이 더 낮다면 합승하지 않아도 된다.
# 특정 구간까지만 합승하고, 중간에 따로 타서 가는 것도 가능
# 모든 노드에서 다른 노드까지의 최소비용을 구하는 알고리즘 - 플로이드-와샬
# 한 노드로부터 다른 노드까지의 최소비용을 구하는 알고리즘 - 다익스트라

# 합승이 끝나는 지점을 k
# return해야 하는 값은 비용(s에서 k까지) + 비용(k에서 a까지) + 비용(k에서 b까지)의 최소비용

import math
def solution(n, s, a, b, fares):
    inf = math.inf
    # 인덱스가 0부터 시작하므로
    s, a, b = s - 1, a - 1, b - 1
    
    # 거리행렬 만들기
    graph = [[inf] * n for _ in range(n)]
    
    for i in fares :
        graph[i[0] - 1][i[1] - 1] = graph[i[1] - 1][i[0] - 1] = i[2] # 각 거리행렬에 주어진 비용 추가
        
    # 플로이드-와샬 알고리즘
    for k in range(n) : # 모든 노드를 중간점(경로)으로 가정하면서
        for i in range(n) : # 거리행렬을 탐색
            for j in range(n) : # 현재 거리행렬에 저장되어 있는 거리가 k를 거쳐가는 거리보다 멀다면 갱신
                if i == j : graph[i][j] = 0 # 자기 자신으로 향하는 거리는 0
                elif graph[i][j] > graph[i][k] + graph[k][j] :
                    graph[i][j] = graph[i][k] + graph[k][j]
    """
    for i in range(n) :
        for j in range(n) :
            print(graph[i][j], '', end='')
        print()
    """
    # 출발점 기준으로 어떤 지점 k를 거쳐 각각 a와 b로 가는 최소 비용 탐색
    answer = graph[s][a] + graph[s][b]
    for k in range(n) :
        if answer > graph[s][k] + graph[k][a] + graph[k][b] :
            answer = graph[s][k] + graph[k][a] + graph[k][b]

    return answer




if __name__ == "__main__" :
    n1, s1, a1, b1 = 6, 4, 6, 2
    fares1 = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    # result = 82
    n2, s2, a2, b2 = 7, 3, 4, 1
    fares2 = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
    # result = 14
    n3, s3, a3, b3 = 6, 4, 5, 6
    fares3 = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
    #result = 18
    
    print(solution(n1, s1, a1, b1, fares1))
    print(solution(n2, s2, a2, b2, fares2))
    print(solution(n3, s3, a3, b3, fares3))