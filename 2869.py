# 2869 달팽이는 올라가고 싶다.
# https://www.acmicpc.net/problem/2869

# 땅 위의 달팽이가 높이가 V미터인 나무 막대를 올라간다.
# 달팽이는 낮에 A미터를 올라갈 수 있지만 밤에 자는동안 B미터 미끄러진다.
# 정상에 올라간 후에는 미끄러지지 않음
# 달팽이가 나무 막대를 모두 올라가려면 며칠이 걸리는지 구하는 프로그램을 작성

# 첫째 줄에 정수 A, B, V가 공백으로 구분되서 주어진다.
import math

A, B, V = map(int, input().split())

"""
시간초과

day = 0
height = 0
while height < V :
    day += 1
    height += A
    
    if height >= V :
        break
    height -= B

print(day)

"""

one = (V - B) / (A - B) # V - B로 해서 정상에 올라간 후 미끄러지는 상황 방지
print(math.ceil(one)) # 올림