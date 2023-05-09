N = int(input())
M = int(input())

if M != 0 :
    button = list(input().split())
else :
    button = []
    
ans = abs(100-N)

# 작은 수에서 큰 수로 500000, 큰 수에서 작은수로 500001 ~ 1000001
for i in range(1000001) :
    for j in str(i) :
        if j in button : # 고장난 버튼
            break
    else :
        ans = min(ans, len(str(i)) + abs(i-N))
        
print(ans)
