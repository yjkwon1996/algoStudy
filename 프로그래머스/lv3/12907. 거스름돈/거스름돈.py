def solution(n, money):
    answer = 0
    
    # 또 dp?
    money.sort()
    dp = [0 for i in range(n+1)] # dp[i]는 i원을 만들 수 있는 경우의 수
    dp[0] = 1 # 초기값. 0원을 만들기 위한 경우의 수는 1개
    
    for value in money :
        for unit in range(value, n+1) :
            dp[unit] = ( dp[unit] + dp[unit-value]) % 1000000007
    
    answer = dp[-1]
    
    return answer