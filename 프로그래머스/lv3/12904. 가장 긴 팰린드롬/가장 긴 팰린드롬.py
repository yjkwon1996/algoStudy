def solution(s):
    answer = 1
    length = len(s)
    arr = [c for c in s]
    dp = [[0 for _ in range(length)] for _ in range(length)]

    for i in range(length) : # 자기 자신 1글자에 대한 팰린드롬은 항상 1
        dp[i][i] = 1
    
    for i in range(length-1) : # 2글자에 대한 팰린드롬
        if arr[i] == arr[i+1] :
            dp[i][i+1] = 1
            answer = 2
    
    for i in range(3, length+1) : # 3글자 이상에 대한 팰린드롬
        for j in range(0, length-i+1) :
            idx = i+j-1 # 팰린드롬 문자열 길이
            if arr[idx] == arr[j] and dp[j+1][idx-1] == 1 : # 팰린드롬에서 좌우로 추가된 문자가 같으면 팰린드롬
                dp[j][idx] = 1
                answer = max(answer, i)
    
    return answer