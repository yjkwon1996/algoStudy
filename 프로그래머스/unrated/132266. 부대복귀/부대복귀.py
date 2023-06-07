from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    
    # 각 부대원들이 복귀하는데 걸리는 최단시간
    # 복귀 부대와 각 부대원들의 거리
    # bfs
    
    visited = [-1 for _ in range(n+1)] # 방문 체크용. 복귀가 불가능하면 최단시간은 -1
    
    graph = [[] for _ in range(n+1)] # 경로 그리기
    for s, t in roads :
        graph[s].append(t)
        graph[t].append(s)
    
    q = deque([destination]) # 복귀 부대에서 시작, 각 부대원들의 거리
    visited[destination] = 0
    
    # bfs
    while q :
        now = q.popleft()
        
        for nxt in graph[now] :
            if visited[nxt] == -1 :
                q.append(nxt)
                visited[nxt] = visited[now] + 1
    
    # 부대원들의 위치만 찾아서 
    answer = [visited[i] for i in sources]
    
    return answer