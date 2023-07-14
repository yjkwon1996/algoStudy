# N개의 정수 A[1] ... A[N]이 주어졌을 때 이 안에 X라는 정수가 존재하는지 알아내기

import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))

for i in find :
    if i in A :
        print(1)
    else :
        print(0)
