# R(뒤집기), D(버리기)
from collections import deque
T = int(input())

for i in range(T) :
    p = input()
    n = int(input())
    arr = input()[1:-1].split(',')  # 배열 형식 입력 받기
    
    q = deque(arr)
    flag = 0 # 뒤집기를 매번 실행해서 시간초과. 뒤집어야 하는지 아닌지 판단. 
    
    if n == 0 : # 빈 배열
        q = []
    
    for i in p :
        if i == 'R' :
            flag += 1
        elif i == 'D' :
            if len(q) != 0 :
                if flag % 2 == 0 : # 삭제하는 요소도 flag에 따라서 제일 앞 혹은 제일 뒤
                    q.popleft()
                else :
                    q.pop()
            else : 
                print('error')
                flag = 0
                break
    
    else :
        if flag % 2 == 0 : # 뒤집기 작업을 안해도 된다면
            print('[' + ','.join(q) + ']')
        else : # 뒤집기 작업을 해야함
            q.reverse()
            print('[' + ','.join(q) + ']')