# 정수를 저장하는 큐를 구현한 다음 입력으로 주어지는 명령을 처리
# push : 큐에 넣기 / pop : 큐에서 가장 앞에 있는 정수를 빼고 출력. 없으면 -1 출력 /
# size : 큐에 들어 있는 정수의 개수 출력 / empty : 큐가 비어 있으면 1, 아니면 0 출력
# front : 큐의 가장 앞에 있는 정수 출력. 없으면 -1 출력
# back : 큐의 가장 뒤에 있는 정수 출력. 없으면 -1 출력

import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) # 명령의 수
q = deque()

for _ in range(N) :
    order = input().split()

    if order[0] == 'push' :
        q.append(order[1])
    elif order[0] == 'pop' :
        if q :
            print(q.popleft())
        else :
            print(-1)
    elif order[0] == 'size' :
        print(len(q))
    elif order[0] == 'empty' :
        if q :
            print(0)
        else :
            print(1)
    elif order[0] == 'front' :
        if q :
            print(q[0])
        else :
            print(-1)
    elif order[0] == 'back' :
        if q :
            print(q[-1])
        else :
            print(-1)
