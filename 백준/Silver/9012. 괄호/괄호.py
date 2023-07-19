

import sys
input = sys.stdin.readline

T = int(input()) # 테스트케이스

for _ in range(T) :
    str = input().rstrip() # rstrip() : 개행문자(\n)이 입력되는 현상 제거
    stack = []
    flag = True
    for i in str :
        if i == '(' : # 여는 괄호는 그냥 추가
            stack.append(i)
        else : # 닫는 괄호는 여는 괄호가 있는지 확인 후
            if stack : # 여는 괄호가 있으면 제거
                stack.pop()
            else : # 여는 괄호가 없으면 NO
                flag = False
                break

    if stack : # 모든 괄호를 탐색했는데 남는 괄호가 있으면 NO
        flag = False

    if flag :
        print('YES')
    else :
        print('NO')