# dfs
def dfs(v) :
    visited[v] = 1
    for next in com[v] : # 연결된 다음 컴퓨터 중
        if visited[next] == 0 : # 아직 감염 안됐으면
            dfs(next) # 감염시키기

num = int(input())
pair = int(input())
com = [[] for i in range(num+1)]
visited = [0]*(num+1)
for i in range(pair) :
    a, b = map(int, input().split())
    com[a].append(b) # 연결된 컴퓨터 쌍
    com[b].append(a) # 양방향

dfs(1) # 1번 컴퓨터를 통해서 감염되는
print(sum(visited)-1) # 모든 컴퓨터의 수

