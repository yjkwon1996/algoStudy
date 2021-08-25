import collections

arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]


"""
이동하는 방향이 담긴 배열 arrows
방의 갯수를 return
사방이 막히면 방 하나 - 일방향의 이어지는 선 하나로 시작점으로 되돌아 올 수 있으면 방 하나
노드가 없는 지점에서 교차함으로써 생기는 방도 고려(|><| 형태)
-> 한번 이동할 때 두 칸씩 이동하도록해서 기존에 노드가 없는 지점에도 노드가 생기도록
방의 생성 여부 - 방문한 노드가 이미 방문한 적이 있고 
해당 노드로 들어온 경로는 처음 이동한 경우 - 지나갔던 경로에 대한 처리
"""
answer = 0
mov = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
position = (0, 0)

visited = collections.defaultdict(lambda : 0) # 노드가 방문한 기록
visited_route = collections.defaultdict(lambda : 0) # 노드 지나간 경로 기록

# 노드 좌표를 큐에 넣어준다
q = collections.deque([position])
for i in arrows :
    for j in range(2) : # (|><| 형태)를 고려하기 위해 2칸씩 
        tmp = (position[0] + mov[i][0], position[1] + mov[i][1])
        q.append(tmp)
        position = tmp
        
position = q.popleft()
visited[position] = 1

while q :
    tmp = q.popleft()
    if visited[tmp] == 1 : # 이미 방문한 노드
        if visited_route[(position, tmp)] == 0: # 경로는 처음일 때
            answer += 1
    else : # 처음 방문한 노드면 체크
        visited[tmp] = 1
        
    # 경로도 체크해 준다
    visited_route[(position, tmp)] = 1
    visited_route[(tmp, position)] = 1
    position = tmp


