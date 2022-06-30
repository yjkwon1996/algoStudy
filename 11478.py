# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/11478
# 11478 서로 다른 부분 문자열의 개수


S = input()
answer = set() # 부분문자열을 저장할 집합

for i in range(len(S)) :
    for j in range(i, len(S)) :
        tmp = S[i:j+1] # 1, 2, 3...씩 증가하면서 문자열 슬라이싱 후 집합에 저장
        answer.add(tmp)
        
print(len(answer))
    






