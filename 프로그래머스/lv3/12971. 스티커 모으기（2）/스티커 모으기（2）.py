def solution(sticker):
    answer = 0
    if len(sticker) == 1 : # 뜯을 수 있는 스티커가 하나인 경우
        answer = sticker[0]
        return answer
        
    # 첫 번째 스티커부터 or 두 번째 스티커부터 dp 계산
    # dp[0] -맨 앞을 뜯는 경우
    # dp[1] -맨 앞을 안 뜯는 경우
    dp = [[0 for _ in sticker] for _ in range(2)]
    dp[0][0] = sticker[0]
    dp[0][1] = sticker[0] # 맨 앞을 뜯은 경우니까 다음껀 못 뜯음
    for i in range(2, len(sticker)-1) : # 맨 앞을 뜯었으니 맨 뒤는 못 뜯음
        dp[0][i] = max(dp[0][i-2]+sticker[i], dp[0][i-1]) # 현재 위치를 뜯어서 추가한 경우와 이전의 것을 뜯은 경우
    for i in range(1, len(sticker)) :
        dp[1][i] = max(dp[1][i-2]+sticker[i], dp[1][i-1])
    
    answer = max(dp[0][-2], dp[1][-1])
    return answer