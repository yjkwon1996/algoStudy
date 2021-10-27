# 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899

"""
10진법이 아닌 1, 2, 4만 사용하는 숫자법
자연수 n이 매개변수로 주어질 때 n을 124나라에서 사용하는 숫자로 바꾼 값을 return
1 = 1, 2 = 2, 3 = 4, 4 = 11
"""

# 1, 2, 4만 사용하는 3진법
# 0이 생기는 것과 3의 값에 대해서 조정이 추가적으로 필요
def solution(n):
    answer = ''

    while n > 0 :
        n -= 1 # 각 자리가 올라갈 때마다 전체 숫자에서 1을 빼준 값을 통해 삽입할 숫자를 정한다.
        answer = '124'[n%3] + answer # 나머지가 0일때는 1, 1일때는 2, 2일때는 4
        n = n//3    
    
    
    return answer



if __name__ == "__main__" :
    n1 = 1 # 1
    n2 = 2 # 2
    n3 = 3 # 4
    n4 = 4 # 11
    print(solution(n1)) 
    print(solution(n2)) 
    print(solution(n3)) 
    print(solution(n4)) 
    
    n5 = 44
    print(solution(n5))