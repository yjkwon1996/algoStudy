# 2775 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775

# 각 층의 사람들을 모아 반상회를 주최
# a층의 b호에 살려면 a-1층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
# 아파트에 비어있는 집은 없고 모든 거주민이 이 계약 조건을 지키고 있다면
# 주어진 양의 정수 k와 n에 대해 k층 n호에는 몇명이 살고 있는지 출력하라.
# 아파트에는 0층부터 있고, 각층에는 1층부터 있으며 0층의 i호에는 i명이 산다.
# 첫번째 입력은 Test case의 수 T
# 각 케이스의 입력마다 첫번째 줄에는 정수 k, 두번째 줄에는 정수 n

# 같은 층 앞 호수의 사람(floor0[j-1])과 아래층 같은 호수의 사람(갱신 전 floor0[j])을 더하면
# 현재 호수에서 살아야 하는 사람의 수가 나온다. 즉 이것은 반복하면됨

def resident(k, n) :
    floor0 = [i for i in range(1, n+1)] # 0층에 각 호수별로 거주하는 사람들
    
    for i in range(k) :     # 각 층별로,
        for j in range(1, n) : # 각 호수별로 몇명이 사는지. 모든 층의 1호는 항상 1명이 살기 때문에 1부터 시작
            floor0[j] += floor0[j-1] # 각 층, 호수를 가면서 갱신해준다.
    
    return floor0[n-1]


T = int(input())
for _ in range(T) :
    k = int(input())
    n = int(input())
    
    print(resident(k, n))
    
    
    
