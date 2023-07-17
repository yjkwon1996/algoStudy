# 길이가 제각각인 K개의 랜선을 모두 N개의 길이가 같은 랜선으로 만들 때
# 최대 랜선의 길이는?

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
line = [int(input()) for _ in range(K)] # K개의 랜선
l, r = 1, max(line) # 이분탐색 시작과 끝

while l <= r : # 랜선의 길이를 토대로 이분탐색하면서 가장 길이가 긴 랜선을 출력하면 된다.
    mid = (l+r) // 2
    cnt = 0 # 랜선 수
    for i in line :
        cnt += i // mid # 랜선 수라는 조건에 만족해야함. 각 랜선들을 mid 길이로 자르기

    # K개의 랜선으로 N개의 랜선을 만들 수 있는 경우는 없다고 가정했기 때문에 아래 이외의 예외는 X
    if cnt >= N : # 잘라서 나온 랜선의 개수가 N개 이상이여야 함
        l = mid + 1 # N개 이상의 랜선이 나온다면, 더 긴 길이로 재탐색
    else : # N개 이하의 랜선이 나온다면 더 짧은 길이로 재탐색
        r = mid - 1

print(r) # 가장 긴 랜선을 출력
