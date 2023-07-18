# 한 개의 회의실을 N개의 회의에 사용
# 각 회의 I에 대해 시작시간과 끝나는 시간이 주어지면 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 최대 개수를 찾기
# 끝나는 시간 순으로 우선 정렬한뒤, 시작하는 시간 순으로 정렬하면?

import sys
input = sys.stdin.readline

N = int(input()) # 회의의 수

conference = []
for _ in range(N) :
    time = list(map(int, input().split()))
    conference.append(time)

conference.sort(key=lambda x: [x[1], x[0]])

answer = 0
last = 0 # 마지막 회의 시간
for start, end in conference :
    if start >= last : # 앞에서부터 회의 추가
        answer += 1
        last = end

print(answer)
