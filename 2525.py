# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2525
# 2525 오븐시계

A, B = map(int, input().split()) # 현재 시, 분
C = int(input()) # 요리에 필요한 시간

h, m = 0, 0
# 시작은 0:0 , 끝은 23:59
if B + C < 60 : # 현재시각에 요리시간을 더해도 60분 미만이면 그대로
    h = A
    m = B + C
else : # 현재시각에 요리시간을 더한 값이 60분을 넘으면 시간 단위로 계산
    h = ((B + C) // 60) + A
    m = (B + C) % 60
    

h = h % 24 # 24시간 초과 시 다음 날로

print(h, m)
