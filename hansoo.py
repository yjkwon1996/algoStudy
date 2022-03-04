# 1065 한수
# https://www.acmicpc.net/problem/1065

# 어떤 양의 정수 x의 각 자리가 등차수열을 이룬다면 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열
# N이 주어졌을 때 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램

def solution(N) :
    cnt = 0 # 한수의 개수를 count
    
    for i in range(1, N+1 ) :
        lst = list(map(int, str(i)))
        
        if i < 100 : # 1 ~ 99는 비교대상이 없기 때문에 모두 한수
            cnt += 1
        elif lst[0] - lst[1] == lst[1] - lst[2] : # 양의 정수 x의 각 자리가 등차수열을 이룬다면
            cnt += 1
        
    return lst

    
N = int(input())
print(solution(N))

# 110 - 99
# 1 - 1
# 210 - 105
# 1000 - 144
# 500 - 1119