# 2017 팁스타운 - 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973
"""
짝지어 제거하기는 알파벳 소문자로 이루어진 문자열 s로 시작.
문자열에서 같은 알파벳이 2개 붙어있는 짝을 찾고, 그 둘을 제거한 뒤 앞뒤로 문자열을 이어 붙인다.
이 과정을 반복해서 문자열을 모두 제거한다면 종료됨
문자열 모두 제거가 가능하다면 1을 return, 할 수 없으면 0을 return
"""

def solution(s):
    stack = []

    for i in range(len(s)) :
        if not stack : # stack이 비어있다면
            stack.append(s[i]) # 값 추가
        else : # 스택이 비어있지 않다면
            if s[i] == stack[-1] : # stack의 마지막 값과 s[i]를 비교하여 같으면 pop
                stack.pop()
            else :
                stack.append(s[i]) # 짝이 안된다면 다음 연산을 위해 stack에 값 추가
    
    if stack : return 0 # stack이 비어있지 않다면 모든 문자열 제거가 안된 경우이기 때문이 0 리턴
    else : return 1 # 반대로 비어있다면 모든 문자열이 제거된 경우. 1 리턴



if __name__ == "__main__" :
    s = 'baabaa' # 1
    s2 = 'cdcd' # 0 
    print(solution(s))
    print(solution(s2))
    
    s3 = 'aabbccdd'
    print(solution(s3))
