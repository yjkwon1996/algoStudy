# 수빈이는 점 N, 동생은 점 K
# 걷거나, 순간이동할 수 있는데 수빈이의 위치가 x라면 걸으면 1초 후에 x-1 or x+1로 이동, 순간이동하면 0초 후에 2*x로 이동
# 동생을 찾을 수 있는 가장 빠른 시간이 몇 초인지 구하기

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
length = 100001
time = [-1 for _ in range(length)]

# bfs로 순간이동하는 경우와 걷는 경우를 나눠서 찾기
q = deque()

# 현재 위치를 추가하고 시작
q.append(N)
time[N] = 0

# 양방향 deque로 순간이동은 appendleft로 앞에 추가하고 걷는 경우는 append로 뒤에 추가
while q :
    now = q.popleft() # 현재 위치
    if now == K :
        print(time[K])
        sys.exit()

    if 0 < now*2 < length and time[now*2] == -1 : # 순간이동이 가능한 거리면 순간이동
        time[now*2] = time[now] # 시간은 변하지 않음
        q.appendleft(now * 2)
    if 0 <= now - 1 >= 0 and time[now-1] == -1 : # x-1 이동
        time[now-1] = time[now]+1
        q.append(now-1)
    if 0 <= now + 1 < length and time[now+1] == -1 : # x+1 이동
        time[now+1] = time[now]+1
        q.append(now+1)


# print(time[K])