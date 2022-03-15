# 10872 팩토리얼
# https://www.acmicpc.net/problem/10872

# 첫째 줄에 정수 N이 주어지고
# 첫째 줄에 N!을 출력한다.
# 재귀 방식으로 풀어낼것

N = int(input())

def factorial(N) :
    if N == 0 : return 1 # n이 0일때는 1
    
    if N == 1 : # n이 1일때 
        return 1 # 1을 반환하고 재귀 종료
    return N * factorial(N - 1)

print(factorial(N))


"""
def factorial(N) :
    result = 1
    if n > 0 :
        result = n * factorial(N - 1)
    return result

print(factorial(N))

"""
