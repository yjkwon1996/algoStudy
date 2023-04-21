N = int(input()) # 도시의 개수
dist = list(map(int, input().split())) # 인접한 두 도시를 연결하는 도로의 길이(dist[1] -> 1~2의 길이)
price = list(map(int, input().split())) # 주유소의 리터당 가격

ans = 0

# 처음에는 다음 도시까지 갈 기름을 충전
ans += price[0] * dist[0]
beforePrice = price[0]
for i in range(1, N-1) :
    # 지금 도시에서 기름값을 비교한 다음
    if (beforePrice < price[i]) : # 지금 도시가 더 비싸면 이전 도시에서 충전
        ans += beforePrice * dist[i]
    else : # 지금 도시가 더 싸면 지금 도시에서 충전
        ans += price[i] * dist[i]
        beforePrice = price[i]
    
print(ans)
        
    