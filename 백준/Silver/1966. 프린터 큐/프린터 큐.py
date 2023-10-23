# 프린터 큐. FIFO 방식 인쇄.
# 이 프린터기는 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
# 예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.
# 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것
# 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다.
# 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

import sys
from collections import deque
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T) :
    N, M = map(int, input().rstrip().split())
    q = deque(list(map(int, input().rstrip().split())))

    cnt = 0
    while q :
        maxi = max(q)
        num = q.popleft() # 하나 꺼내고
        M -= 1 # 내 위치도 한칸 앞으로

        if num == maxi : # 꺼낸 값이 큐에서 최댓값이면
            cnt += 1 # 그 값 제거
            if M < 0 : # 제거했는데 M이 0보다 낮아졌다 -> N을 찾은 경우
                print(cnt)
                break
        else : # 꺼낸 값이 최댓값이 아니면
            q.append(num) # 맨 뒤에 다시 넣으면 됨
            if M < 0 : # N 값을 찾았는데, 최댓값을 먼저 뽑은 경우가 아님
                M = len(q) - 1 # 맨 뒤 위치로 다시






