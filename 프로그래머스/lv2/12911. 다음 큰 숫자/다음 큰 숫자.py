def check(n, one) :
    if one == bin(n).count('1') : # 2진수로 변환했을 때 1의 갯수가 같음
        return True
    return False

def solution(n):
    answer = 0
    cnt = bin(n).count('1')
    for i in range(n+1, 1000001) :
        if check(i, cnt) :
            answer = i
            break
        
    return answer