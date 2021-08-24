from collections import deque

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	

"""
n개의 노드가 있는 그래프, 1~n까지의 번호
노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex. 간선은 양방향
1번노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return
"""
answer = 0
# 딕셔너리에 노드별 연결정보를 저장
routes = dict()
for a, b in edge :
    routes.setdefault(a, []).append(b) # key, value
    routes.setdefault(b, []).append(a)
    
q = deque([[1, 0]]) # 노드번호, 깊이
co = [-1] * (n+1)
while q :
    idx, dist = q.popleft() # 큐에서 꺼낼 때, 노드번호 = 깊이
    co[idx] = dist
    for i in routes[idx] :
        if co[i] == -1 : # 탐색하지 않은 노드를 탐색하면 0으로
            co[i] = 0 
            q.append([i, dist+1])
    dist += 1
print(co)
answer = co.count(max(co))
