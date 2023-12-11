# 구간 합 구하기. 어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다.
# 만약에 1,2,3,4,5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 합을 구하라고 한다면 17을 출력하면 되는 것이다.
# 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 합을 구하라고 한다면 12가 될 것이다.
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다.
# M은 수의 변경이 일어나는 횟수이고, K는 구간의 합을 구하는 횟수이다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다.
# 그리고 N+2번째 줄부터 N+M+K+1번째 줄까지 세 개의 정수 a, b, c가 주어지는데,
# a가 1인 경우 b(1 ≤ b ≤ N)번째 수를 c로 바꾸고 a가 2인 경우에는 b(1 ≤ b ≤ N)번째 수부터 c(b ≤ c ≤ N)번째 수까지의 합을 구하여 출력하면 된다.
# 입력으로 주어지는 모든 수는 -263보다 크거나 같고, 263-1보다 작거나 같은 정수이다.

# 첫째 줄부터 K줄에 걸쳐 구한 구간의 합을 출력한다. 단, 정답은 -263보다 크거나 같고, 263-1보다 작거나 같은 정수이다.

# import sys
# input = sys.stdin.readline
#
# N, M, K = map(int, input().rstrip().split())
#
# num = [int(input().rstrip()) for _ in range(N)]
#
# while K :
#     a, b, c = map(int, input().rstrip().split())
#     if a == 1 :
#         num[b-1] = c
#     elif a == 2 :
#         print(sum(num[b-1:c]))
#         K -= 1

# 세그먼트 트리

import sys
input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())

num = [int(input().rstrip()) for _ in range(N)]
tree = [0 for _ in range(4*N)] # 트리 공간은 N의 4배만큼 필요

# 세그먼트 트리 만들기
def buildTree(x, left, right) :
    # 마지막에 도착
    if left == right :
        tree[x] = num[left]
        return tree[x]

    mid = (left + right) // 2
    # 왼쪽 노드
    leftNode = buildTree(x*2, left, mid)
    # 오른쪽 노드
    rightNode = buildTree(x*2+1, mid+1, right)
    tree[x] = leftNode + rightNode
    return tree[x]

# 세그먼트 트리 수정(b위치의 숫자를 c로 변경)
def updateTree(b, c, x, left, right) :
    # b 위치 발견
    if left == right == b :
        tree[x] = c
        return

    # b 위치를 찾지 못함
    if left > b or right < b :
        return

    mid = (left + right) // 2
    # 연관된 왼쪽 자식 노드도 다 바꿔야하고
    updateTree(b, c, x*2, left, mid)
    # 오른쪽도 바꿔야 함
    updateTree(b, c, x*2+1, mid+1, right)
    # 현재 노드
    tree[x] = tree[x*2] + tree[x*2+1]

# 세그먼트 트리 합 구하기
def sumTree(b, c, x, left, right) :
    # 구하고 싶은 구간(b~c)가 현재 트리 구간에 없으면
    if left > c or right < b :
        return 0
    # 구하고 싶은 구간이 있다면
    if left >= b and right <= c :
        return tree[x]
    # 구간이 겹치면
    mid = (left + right) // 2
    leftNode = sumTree(b, c, x*2, left, mid)
    rightNode = sumTree(b, c, x*2+1, mid+1, right)
    return leftNode + rightNode


buildTree(1, 0, N-1)
# print(tree)
while K :
    a, b, c = map(int, input().rstrip().split())
    if a == 1 :
        updateTree(b-1, c, 1, 0, N-1)
        # print(tree)
    elif a == 2 :
        print(sumTree(b-1, c-1, 1, 0, N-1))
        K -= 1



