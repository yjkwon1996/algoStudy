# -*- coding: utf-8 -*-
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금

# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")

# 한칸씩 위치를 변경해가면서, 변경할 수 있는 기회를 생각.
# 최종적으로 최대값을 찾으면 된다.
# dfs를 반복하면서 위치를 변경하면서, 변경할 수 있는 기회를 하나씩 차감
# 정렬을 다해도 기회가 남으면 마지막 두칸을 계속해서 교환
# 기회를 다썼다면 이전까지 탐색했던 값들 중 최댓값을 찾아서 출력
def dfs(idx, check) :
    global answer
    if check == chance :
        answer = max(int(''.join(map(str, arr))), answer)
        return
    for i in range(idx, length) :
        for j in range(i+1, length) :
            if arr[i] <= arr[j] :
                arr[i], arr[j] = arr[j], arr[i]
                dfs(idx, check+1)
                arr[i], arr[j] = arr[j], arr[i]
    if not answer and check < chance :
        if (check-chance) % 2 :
            arr[-1], arr[-2] = arr[-2], arr[-1]
        dfs(idx, chance)
        

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num, chance = map(int, input().split())
    
    arr = list(map(int, str(num)))
    length = len(arr)
    answer = 0
    dfs(0, 0)

print("#{} {}".format(test_case, answer))

