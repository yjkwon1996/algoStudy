# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1269
# 1269 대칭 차집합

Acnt, Bcnt = map(int, input().split())

A = set(map(int, input().split())) 
B = set(map(int, input().split())) 

Anum = len(A - (A & B)) 
Bnum = len(B - (A & B))

print(Anum+Bnum)


