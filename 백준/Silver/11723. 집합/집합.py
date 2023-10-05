# 집합. 비어있는 공집합 S가 주어지면 다음 연산을 수행하라
# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

import sys
input = sys.stdin.readline

M = int(input().rstrip())

S = set()
for _ in range(M) :
    order = input().rstrip().split()

    if len(order) == 1 : # 시간초과 해결용
        if order[0] == 'all':
            S = set([i for i in range(1, 21)])  # 집합을 (1, 2, 3 ... 20)으로. 기존에 문자형으로 다 입력했음...
        else:
            S = set()
        continue

    od = order[0]
    x = int(order[1])

    if od == 'add' :
        S.add(x)
    elif od == 'remove' :
        S.discard(x) # remove : 제거하지만 없으면 에러 / discard : 제거하지만 없으면 무시
    elif od == 'check' :
        if x in S :
            print(1)
        else :
            print(0)
    elif od == 'toggle' :
        if x in S :
            S.discard(x)
        else :
            S.add(x)






