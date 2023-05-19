def solution(n):
    answer = 0
    for i in range(1, n//2+1) :
        sum = 0
        cnt = i
        while sum < n :
            sum += cnt
            if sum == n :
                answer += 1
                break
            cnt += 1
    
    answer += 1 # 마지막에 자기 자신의 수(15 = 15)
    return answer