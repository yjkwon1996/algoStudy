# -*- coding: utf-8 -*-
# 14888 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

"""
N개의 수로 이루어진 수열 A1, A2, A3 ... AN과
수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자(덧셈, 뺼셈, 곱셈, 나눗셈)가 주어진다.
수와 수 사이에 연산자를 하나씩 넣어서 수식을 만들 수 있다. 주어진 수의 위치를 변경하면 안됨
1, 2, 3, 4, 5, 6과 덧셈 2개, 뺄셈 1개, 곱셈 1개, 나눗셈 1개인 경우 총 60개의 수식을 만들 수 있음
식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행
나눗셈은 정수 나눗셈으로 몫만 취한다.
음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 계산하고 그 몫을 음수로 바꾸는 형식으로
N개의 수와 N-1개의 연산자가 주어졌을 때 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램
"""
# 입력 : 첫째 줄에 수의 개수 N(2 <= N <= 11). 둘째 줄에는 A1, A2, A3 , ... , AN(1 <= A <= 100)
# 셋째 줄에는 합이 N-1인 4개의 정수. 차례대로 덧셈, 뺄셈, 곱셈, 나눗셈의 개수가 공백으로 구분되어 주어짐
# 출력 : 첫째 줄에 만들 수 있는 결과의 최댓값을, 둘째 줄에는 최솟값 출력
# 결과값과 중간값의 최소, 최대크기는 항상 -10억 ~ 10억 사이


N = int(input())

num = list(map(int, input().split())) # A1, A2...
operator = list(map(int, input().split())) # 연산자

max_num = -1000000000
min_num = 1000000000

# 최댓값과 최솟값 두가지 값을 찾는 백트래킹
def dfs(depth, result, plus, minus, multiply, divide) :
    global max_num, min_num
    
    if depth == N : # N개의 정수를 다 계산했다면 그 결과와 이전의 최대, 최솟값을 비교하여 갱신
        max_num = max(max_num, result)
        min_num = min(min_num, result)
        return
    
    
    if plus > 0 :
        dfs(depth+1, result+num[depth], plus-1, minus, multiply, divide)

    if minus > 0 :
        dfs(depth+1, result-num[depth], plus, minus-1, multiply, divide)

    if multiply > 0 :
        dfs(depth+1, result*num[depth], plus, minus, multiply-1, divide)

    if divide > 0 : # // 계산으로는 음수 나눗셈에서 틀린 값을 내기 때문에 int(a/b)로 계산
        dfs(depth+1, int(result/num[depth]), plus, minus, multiply, divide-1)

        
dfs(1, num[0], operator[0], operator[1], operator[2], operator[3])
print(max_num)
print(min_num)
