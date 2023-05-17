def solution(s):
    answer = True
    
    arr = list(s)
    ans = []
    for i in arr :
        if i == '(' :
            ans.append(i)
        else : # ')' 문자가 나왔는데
            if not ans : # 앞에 '('가 없었다면 끝
                return False
            else : # 앞에 '('가 있으면 스택에서 제거
                ans.pop()
    
    # 마지막까지 다 봤는데 스택에 남아있으면 false
    if ans : return False
    return True