# 전쟁 - 땅따먹기. 드디어 전쟁은 전면전이 시작되었고, 서로 땅을 따먹기 시작했다.
#
# 현재 여러 지역은 한창 전쟁이 벌어지고 있는 상황인데, 어느 지역은 거의 전쟁이 마무리 단계로 가고 있다.
#
# 하지만 당신은 군대를 보낼 때 적군을 혼란시키기 위해서 우리 나라의 군대라는걸 표시하지 않고, 군대의 번호로 표시했다.
#
# 어느 땅에서 한 번호의 군대의 병사가 절반을 초과한다면 그 땅은 그 번호의 군대의 지배하에 놓이게 된다.
#
# 이때, 각 땅들을 지배한 군대의 번호를 출력하여라. 만약, 아직 전쟁이 한창중인 땅이라면 “SYJKGW”을 쌍 따옴표 없이 출력한다.
#
# 입력
# 첫째 줄에는 땅의 개수 n(n<=200)이 주어진다. 그리고 두 번째 줄에서 n+1번째 줄에는 제일 처음에 숫자 Ti(i번째 땅의 병사수, Ti<=100,000)와, Ti개의 숫자 (각각 병사의 군대 번호)가 주어진다.
# i번째 땅의 j번째 병사 번호 Nij가 주어진다. ( | Nij | <= 2^31 )
#
# 출력
# 첫째 줄에는 각각의 땅의 상태를 순서대로 출력한다. 만약 땅이 지배가 되어있다면 그 지배한 병사의 번호를 출력하고, 아니라면 “SYJKGW”을 쌍 따옴표 없이 출력한다.

import sys
input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n) :
    cnt = dict()
    value = input().rstrip().split()
    Ti = int(value[0])

    maxCnt = 0
    maxKey = 0
    for i in range(1, Ti+1) :
        num = int(value[i])
        if num not in cnt :
            cnt[num] = 1
        else :
            cnt[num] += 1

        if cnt[num] > maxCnt :
            maxCnt = cnt[num]
            maxKey = num

    if maxCnt > Ti / 2:
        print(maxKey)
    else :
        print("SYJKGW")











