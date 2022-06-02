# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2884
# 2884 알람시계

H, M = map(int, input().split())

# 시작은 0:0 , 끝은 23:59
if M - 45 >= 0 : # 45분 일찍
    M -= 45
else : # 45분이 모자라면 1시간을 60분으로
    M += 60 - 45
    H -= 1
    
if H < 0 : # 0시간 아래면 그 전날 울리도록
    H = 23

print(H, M)
