# 소수 구하기
M, N = map(int, input().split()) # M 이상, N 이하의 소수를 구하기

for i in range(M, N+1) :
    if i == 1 : # 1은 소수가 아님
        continue
    for j in range(2, int( i ** 0.5 )+1) : # i의 제곱근까지만 탐색하면 됨
        if i%j == 0 : # 나머지가 0 -> 소수가 아님
            break
    else : # for문을 다 돌았는데 break 되지 않았다면
        print(i)
