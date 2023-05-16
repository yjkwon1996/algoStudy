from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split())) 

ans = 0
for i in range(1, N+1) :
    com = combinations(arr, i)
    for tmp in com :
        if sum(tmp) == S :
            ans += 1
            
print(ans)