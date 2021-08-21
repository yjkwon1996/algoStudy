
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

"""
항상 ICN에서 출발. 항공권 정보가 담긴 2차원 배열 tickets
방문하는 경로를 배열에 담아 return
모든 항공권 사용, 모든 도시를 방문해야 함
가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return
정렬 사용시 경로 오류?
시작 - 도착 그래프. 도착점의 리스트는 역순 정렬, DFS 알고리즘으로 모두 탐색
ICN을 스택에 넣고, 스택이 빌 때까지
스택 가장 위의 데이터를 꺼낸다. 없거나 시작점이 다르면 스택에서 꺼내와 경로에 저장
시작점이 있으면 그 데이터의 도착점을 시작점으로 하는 것중 마지막 지점을 꺼내 스택에 저장
"""
answer = []

# 그래프 생성
route = dict()

for start, end in tickets :
    route[start] = route.get(start, []) + [end]
    
# 시작점-끝점 역순정렬
for i in route.keys() :
    route[i].sort(reverse=True)
    
# DFS 알고리즘으로 경로 탐색
arr = ["ICN"]
path = []

while arr :
    st = arr[-1]
    if st not in route or len(route[st]) == 0 :
        path.append(arr.pop())
    else : 
        arr.append(route[st][-1])
        route[st] = route[st][:-1]
        
# 만든 path를 거꾸로
answer = path[::-1]

answer