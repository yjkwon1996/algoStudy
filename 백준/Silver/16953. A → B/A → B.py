# A → B. 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
#
# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다.
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.
#
# 입력
# 첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.
#
# 출력
# A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.

import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())

q = deque()
q.append((A, 1))

while q :
    now, cnt = q.popleft()

    if now == B :
        print(cnt)
        sys.exit()

    if now > B : # 현재 수가 B보다 큰 수면 B 불가능
        continue

    q.append((now*2, cnt+1)) # *2
    q.append((int(str(now)+"1"), cnt+1)) # 뒤에 1 추가

print(-1) # 불가능


