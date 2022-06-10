# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1620
# 1620 나는야 포켓몬 마스터 이다솜


"""
# 시간초과

N, M = map(int, input().split()) # 도감에 수록되어있는 포켓몬의 개수 N, 내가 맞춰야하는 문제의 개수 M

# N개의 줄에 1~N번의 포켓몬 이름이 주어짐
book = []
for i in range(N) :
    book.append(input())

# M개의 줄에 문제가 입력됨. 알파벳 - 해당하는 포켓몬 번호 의 입력 - 출력 관계
for i in range(M) :
    q = input()
    if q.isdigit() : # 숫자가 입력되면 해당하는 번호의 포켓몬 이름
        print(book[int(q)-1])
    else : 
        print(book.index(q)+1) # 문자가 입력되면 해당하는 포켓몬 번호

"""

import sys

N, M = map(int, sys.stdin.readline().split()) # 도감에 수록되어있는 포켓몬의 개수 N, 내가 맞춰야하는 문제의 개수 M

# N개의 줄에 1~N번의 포켓몬 이름이 주어짐
book = dict()
for i in range(1, N+1) : # 번호 : 이름 / 이름 : 번호 쌍을 같은 딕셔너리에 저장해서 찾기 편하게
    tmp = sys.stdin.readline().rstrip()
    book[i] = tmp
    book[tmp] = i


# M개의 줄에 문제가 입력됨. 알파벳 - 해당하는 포켓몬 번호 의 입력 - 출력 관계
for i in range(M) :
    q = sys.stdin.readline().rstrip()
    if q.isdigit() : # 숫자가 입력되면 해당하는 번호의 포켓몬 이름
        print(book[int(q)])
    else : 
        print(book[q]) # 문자가 입력되면 해당하는 포켓몬 번호

