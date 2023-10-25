# 제로. 첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)
# 이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
# 정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.
# 이렇게 모든 수를 받아 적은 후 그 수의 합을 출력

import sys
input = sys.stdin.readline

K = int(input().rstrip())
stack = []
for _ in range(K) :
    num = int(input().rstrip())

    if num == 0 :
        stack.pop()
    else :
        stack.append(num)

print(sum(stack))



