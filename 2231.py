# 2231 분해합
# https://www.acmicpc.net/problem/2231

"""
어떤 자연수 N이 있을 때 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 말한다.
어떤 자연수 M의 분해합이 N인 경우 M을 N의 생성자라 한다.
245의 분해합은 256(=245 + 2 + 4 + 5). 따라서 245는 256의 생성자가 된다.
어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로 생성자가 여러개인 자연수도 있을 수 있다.
자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성
"""
    
# 자연수 N 입력, 답 출력. 생성자가 없으면 0 출력
# 생성자의 범위는 (자릿수 * 9). 256의 생성자의 범위는 256 - (3 * 9 = 27)
# 그 범위 내의 모든 값을 더하면서 생성자를 찾으면 된다.
"""
def solution(N) :
    
    for i in range(N - 9*len(str(N)), N) :
        tmp = i + sum(map(int, str(i)))
        if N == tmp :
            return i  
        
    return 0

N = int(input())

print(solution(N))
    
"""

N = int(input())

min = N - 9*len(str(N))
min = 1 if min < 1 else min # 처음 시작 범위를 조정해줘야 런타임에러가 발생하지 않음

for i in range(min, N+1) : # 여기서, 최소 시작 범위 때문에 런타임 에러가 발생할 수 있음.
    tmp = i + sum(map(int, str(i)))
    if N == tmp :
        print(i)
        break
    if i == N :
        print('0')