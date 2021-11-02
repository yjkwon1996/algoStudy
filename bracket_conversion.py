# 2020 KAKAO BLIND RECRUITMENT
# https://programmers.co.kr/learn/courses/30/lessons/60058

"""
1. 입력이 빈 문자열인 경우 빈 문자열을 반환
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
   단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
"""

# 균형잡힌 괄호 문자열 p가 주어지면 올바른 괄호 문자열로 변환한 결과를 return

# u, v 분리
def divide(p) :
    # 균형잡힌 문자열 분리
    left_p = 0
    right_p = 0
    for i in range(len(p)) :
        if p[i] == '(' : # '(' 괄호의 수
            left_p += 1
        else : 
            right_p += 1 # ')' 괄호의 수
        if left_p == right_p : # '('와 ')'의 수가 같아지면 균형잡힌 문자열
            u = p[:i + 1]
            v = p[i + 1:]
            return u, v

# 올바른 괄호 문자열인지 확인
def check(u) :
    stack = []
    for i in u :
        if i == '(' :
            stack.append(i)
        else :
            if not stack : return False # 스택에 '('가 없는데')' 가 나온다면 잘못된 문자열이므로 False
            stack.pop()
    return True # '('와 ')'의 수가 동일하다 = 올바른 괄호 문자열

def solution(p):
    
    # 1. 입력이 빈 문자열인 경우 빈 문자열 반환
    if not p: 
        return ""
    
    # 2. 문자열분리
    u, v = divide(p)
    
    # 3. u가 올바른 괄호 문자열이라면 v에 대해서 1단계부터 다시 수행. 
    # 수행한 결과 문자열을 u에 이어붙인 후 반복
    if check(u) : return u + solution(v)
    # 4. 올바른 괄호 문자열이 아니라면 4-1 ~ 4-5 수행
    else :
        answer = '(' # 4-1
        answer += solution(v) # 4-2
        answer += ')' # 4-3
        
        for i in u[1:len(u) - 1] : # 4-4. u의 첫번째와 마지막 문자열 제거
            if i == '(' : # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 추가
                answer += ')'
            else : answer += '('

    return answer



if __name__ == "__main__" :
    p1 = "(()())()" # "(()())()"
    p2 = ")(" # "()"
    p3 = "()))((()" # "()(())()"
    print(solution(p1))
    print(solution(p2))
    print(solution(p3))