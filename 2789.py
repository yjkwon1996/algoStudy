# 2789 블랙 잭
# https://www.acmicpc.net/problem/2798

# 블랙잭은 카드의 합이 21을 넘지 않는 한도 내에서 카드의 합을 최대한 크게 만드는 게임
# 각 카드에는 양의 정수가 적혀 있고, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다.
# 그런 후에 딜러는 숫자 M을 크게 외치고, 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장을 고른다.
# 3장의 합은 M을 넘지 않되, M가 최대한 가깝게 만들어야 한다.
# N장의 카드에 써져 있는 숫자가 주어질 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력

# 첫째 줄에 카드의 개수 N이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어진다.
# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어짐
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

# 첫째 줄에 N M 입력, 둘째 줄에 카드에 있는 수가 주어짐.

"""
N, M = map(int, input().split())

num_arr = list(map(int, input().split()))

answer = 0
for i in range(0, N-2) : # 3장의 반복문을 통해서 각각의 모든 경우의 수를 발견
    for j in range(i+1, N-1) :
        for k in range(j+1, N) :
            if (num_arr[i] + num_arr[j] + num_arr[k] > M) : # 3장의 합이 M을 넘어서면 예외
                continue
            else :
                answer = max(answer, num_arr[i] + num_arr[j] + num_arr[k]) # 넘지 않는 선에서 최대값 발견

print(answer)
"""

# permutation(순열)을 쓸 수 있지 않을까??

from itertools import permutations
N, M =  map(int, input().split())
num_arr = list(map(int, input().split()))

permutations_arr = permutations(num_arr, 3) # num_arr에서 3장을 찾아서 조합
answer = 0
for i in permutations_arr : 
    if (M >= sum(i)) : # 3장의 합이 M을 넘지 않는 조합에서 최대값 발견
        answer = max(answer, sum(i))
print(answer)

# 정답. 가능하다! 하지만 시간이 위에는 156ms인데 비해 permutations를 쓰면 564ms가 걸림...
