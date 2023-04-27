import sys

X, Y = map(int, input().split())
Z = Y * 100 // X

left, right = 1, 1000000001
ans = sys.maxsize
while left <= right : 
    mid = (left + right) // 2
    victory = (Y + mid) * 100 // (X + mid)
    
    if victory > Z : # 승률이 커졌으면
        ans = min(ans, mid) # 승률이 변하는 최소값을 찾아야함
        right = mid - 1
    else :
        left = mid + 1
        
if ans == sys.maxsize : # 승률 변화가 없는 경우, 더 오를 수 없음
    print(-1)
else :
    print(ans)