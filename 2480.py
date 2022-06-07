# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2480
# 2480 주사위 세개

# 주사위 3개의 눈
a, b, c = map(int, input().split())
money = 0

# 같은 눈 세개 - 10000 + (같은 눈)*1000
if a == b == c :
    money = 10000 + a*1000

# 같은 눈 두개 - 1000 + (같은 눈)*100
elif a == b or a == c :
    money = 1000 + a*100
elif b == c :
    money = 1000 + b*100

# 모두 다른 눈 - (가장 큰 눈)*100
else :
    money = max(a, b, c)*100
    
print(money)



