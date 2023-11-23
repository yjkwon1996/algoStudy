# 공유기 설치. 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
# 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다.
# 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다.
# 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.
# 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.

import sys
input = sys.stdin.readline

N, C = map(int, input().rstrip().split())
home = list(int(input().rstrip()) for _ in range(N))
home = sorted(home)

left = 1
right = home[-1] - home[0]

# 이진탐색으로 앞 집부터 공유기를 설치하되, 간격을 mid로 하여 설치.
# 설치할 수 있는 공유기가 C보다 많다면 mid+1, 반대면 -1
answer = 0
while left <= right :
    mid = (left+right) // 2
    now = home[0]
    cnt = 1

    for i in range(1, N) :
        if home[i] >= now + mid : # mid의 간격보다 크거나 같은 간격으로 설치하기
            cnt += 1
            now = home[i]

    if cnt >= C : # 설치한 공유기의 수가 C보다 많거나 같다면
        left = mid+1
        answer = mid
    else :
        right = mid-1

print(answer)







