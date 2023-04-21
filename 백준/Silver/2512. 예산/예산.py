N = int(input())
budget = list(map(int, input().split()))
M = int(input())

start, end = 0, max(budget)
# 이분 탐색. 
while start <= end :
    mid = (start+end) // 2
    value = 0 # 총 지출
    for i in budget :
        if i > mid : 
            value += mid
        else : 
            value += i
    if value <= M : # 총 지출이 예산보다 작으면 그대로
        start = mid+1
    else : # 예산보다 큰 지출
        end = mid-1
print(end)