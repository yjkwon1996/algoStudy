# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/10816
# 10816 숫자카드2

from collections import Counter

N = int(input())
card = list(map(int, input().split()))
M = int(input())
search = list(map(int, input().split()))

cnt = Counter(card) # Counter 사용 - {x : y} x값이 y개 있다 형식으로 주어짐

for i in search :
    print(cnt[i], end=' ') # i값이 몇개있는지 출력


