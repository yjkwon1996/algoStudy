def solution(s):
    answer = ''
    s = s.split(' ') # 문자열을 공백 기준으로 나누고
    
    ans = []
    for c in s :
        c = c.capitalize()
        ans.append(c)
    
    answer = " ".join(ans)
    return answer