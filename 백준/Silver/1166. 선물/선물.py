# 민식이는 아이들에게 선물할 같은 크기의 작은 박스를 N개 가지고 있다. 모든 작은 박스는 정육면체이고, 크기는 A × A × A 이다.
# 민식이는 이 작은 박스를 크기가 L × W × H 인 직육면체 박스에 모두 넣으려고 한다. 모든 작은 박스는 큰 박스 안에 있어야 하고, 작은 박스의 변은 큰 박스의 변과 평행해야 한다.
# N, L, W, H가 주어질 때, 가능한 A의 최댓값을 찾는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 네 정수 N, L, W, H가 주어진다.
# 출력
# 첫째 줄에 가능한 A의 최댓값을 출력한다. 절대/상대 오차는 10-9까지 허용한다.

import sys
input = sys.stdin.readline

N, L, W, H = map(int, input().rstrip().split())

left = 0
right = max(L, W, H)

for _ in range(10000) :
    mid = (left+right) / 2
    cnt = (L//mid) * (W//mid) * (H//mid)
    if cnt >= N :
        left = mid
    else :
        right = mid

print('%.10f' %(right))


