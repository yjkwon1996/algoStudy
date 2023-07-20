# 나무 M미터가 필요. 절단기를 이용해서 절단기 위치 이상의 높이의 나무를 잘라서
# 필요한 만큼만 가져가기. 최소 M미터의 나무를 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하기

import sys
iput = sys.stdin.readline

N, M = map(int, input().split()) # 나무수 N, 가져가려는 나무의 길이 M
tree = list(map(int, input().split()))

# 이분 탐색으로 높이의 최댓값을 찾기
l, r = 1, max(tree)

while l <= r :
    mid = (l + r) // 2 # 절단기 위치

    sum = 0 # 벌목한 나무의 높이 계산용
    for t in tree :
        if t >= mid :
            sum += t-mid

    if sum < M : # 저른 높이의 합이 부족하다면, 더 낮은 높이에서 잘라야함
        r = mid - 1
    else : # 자른 높이의 합이 M 이상이면 더 높은 위치에서 잘라보기
        l = mid + 1

print(r)



