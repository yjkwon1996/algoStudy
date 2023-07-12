# union-find
# 합집합 연산. 두 원소가 같은 집합에 포함되어 있는지 구하기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)  # 재귀 한도 늘리기

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]  # 0 ~ n까지의 집합


def find(x):  # 같은 집합에 포함되어 있는지 확인
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):  # 두 원소를 같은 집합에 합하기
    a = find(a)
    b = find(b)
    if a < b : # 수가 더 낮은 쪽이 부모
        parent[b] = a
    else :
        parent[a] = b


for _ in range(m):
    order, a, b = map(int, input().split())
    if order == 0 : # 합연산
        union(a, b)
    else : # 확인 연산
     if find(a) == find(b) : # 두 원소가 같은 집합에 포함되면
        print("YES")
     else :
        print("NO")

