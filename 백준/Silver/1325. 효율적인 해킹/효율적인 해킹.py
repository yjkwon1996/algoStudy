# N개의 컴퓨터, A가 B를 신뢰하는 경우 B를 해킹하면 A도 해킹가능 - 단방향?
# 신뢰하는 관계가 주어지면
# 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 번호를 오름차순으로 출력

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]

for i in range(M) :
    A, B = map(int,input().rstrip().split()) # A가 B를 신뢰하는 경우 B를 해킹하면 A도 해킹가능
    graph[B].append(A) # B->A로 영향이 퍼져야 함

# bfs?
def bfs(x) :
    q = deque([x]) # iterable
    cnt = 1
    visited = [False for _ in range(N+1)]
    visited[x] = True

    while q :
        point = q.popleft()
        for i in graph[point] :
            if not visited[i] :
                visited[i] = True
                q.append(i)
                cnt += 1

    return cnt

# 각 컴퓨터마다 몇 대까지 해킹하는지 계산 후 저장
answer = []
for i in range(1, N+1) :
    answer.append(bfs(i))

# 앞에서부터 확인하면서 그 중 최댓값과 동일한 값이 있다면 출력 -> 자동으로 오름차순 출력
for i in range(len(answer)) :
    if answer[i] == max(answer):
        print(i+1, end = ' ') # 0부터 계산했으므로 결과는 +1한 값으로



