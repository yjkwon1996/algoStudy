# 여행에 필요하다고 생각되는 N개의 물건
# 각 물건은 W의 무게와 V의 가치를 가짐. 최대 무게는 K
# 냅색 알고리즘

N, K = map(int, input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
stuff = [[0, 0]] # 물건 목록을 [무게, 가치]로

for i in range(N) :
    W, V = map(int, input().split())
    stuff.append([W, V])

# 냅색
for i in range(1, N+1) :
    for j in range(1, K+1) :
        w = stuff[i][0]
        v = stuff[i][1]
        
        if j < w : # 물건을 못담는 무게면 위를 그대로
            dp[i][j] = dp[i-1][j]
        else : # 물건을 담을 수 있다면 최대 효율을 내는 물건을 담기
            dp[i][j] = max(v+dp[i-1][j-w], dp[i-1][j])

print(dp[-1][-1])
            

