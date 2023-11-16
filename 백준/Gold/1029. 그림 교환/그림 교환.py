# 그림 교환. 예술을 사랑하는 사람들이 시장에 모여서 그들의 그림을 서로 거래하려고 한다. 모든 그림의 거래는 다음과 같은 조건을 만족해야 한다.
# 그림을 팔 때, 그림을 산 가격보다 크거나 같은 가격으로 팔아야 한다.
# 같은 그림을 두 번 이상 사는 것은 불가능하다.
# 방금 시장에 새로운 그림이 들어왔다. 1번 아티스트는 그 그림을 외부 상인에게 가격 0을 주고 샀다. 이제 그 그림을 자신의 예술가 친구들에게 팔려고 한다.
# 위의 조건을 모두 만족하는 거래만 이루어진다고 가정했을 때, 그림을 소유했던 사람의 수의 최댓값을 출력하는 프로그램을 작성하시오. (1번 아티스트와 마지막으로 그 그림을 소유한 사람도 포함한다).
#
# 첫째 줄에 예술가의 수 N이 주어진다. N은 2보다 크거나 같고, 15보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에는 N개의 수가 주어진다. i번째 줄의 j번째 수는 j번 예술가가 i번 예술가에게 그 그림을 살 때의 가격이다. 모든 가격은 0이 제일 낮은 가격이고, 9가 제일 높은 가격이다.
# 첫째 줄에 그 그림을 소유 했던 사람들 (잠시라도 소유했던 사람도 포함)의 최댓값을 출력한다.
# https://velog.io/@gobeul/%EB%B0%B1%EC%A4%80-1029-%EA%B7%B8%EB%A6%BC-%EA%B5%90%ED%99%98-python-java 여기 보고 참고했음... 모르겠어


import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input().rstrip())
price = [list(map(int, input().rstrip())) for _ in range(N)]

dp = defaultdict(list)
dp[1] = [[0 for _ in range(10)] for _ in range(N) ]
# dp[x][y][z] -> 그림을 보유했던 상황이 x인 상태에서 마지막으로 y가 z원에 샀을 때

def dfs(past, current, value) :
    # past : 과거에 그림을 소유했던 사람
    # current : 현재 그림을 가지고 있는 사람
    # value : 현재 그림 가격
    if not dp[past] :
        dp[past] = [[0 for _ in range(10)] for _ in range(N)]

    if dp[past][current][value] != 0 : # 이미 거래한 기록이 존재(같은 그림을 두 번 이상 사는것은 불가능)
        return dp[past][current][value]

    cnt = 0
    for i in range(N) :
        if past & 1 << i == 0 : # past에서는 i가 아직 그림을 못 만져봄
            if value <= price[current][i] : # value 가격에 current가 i에게 판매 가능
                cnt = max(cnt, dfs(past | 1 << i, i, price[current][i])+1)

    dp[past][current][value] = cnt
    return cnt

print(dfs(1, 0, 0)+1)



