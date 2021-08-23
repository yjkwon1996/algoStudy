
n = 6
times = [7, 10]

"""
입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 time
모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return
이분 탐색 : left, right로 나눈 중간값 mid로부터 값을 비교하며 탐색
범위 : 심사하는데 걸리는 시간
기준 : mid동안 심사한 사람 수가 n보다 많으면 시간이 충분 -> 시간을 줄인다
n보다 적으면 시간이 부족 -> 시간을 늘린다
"""
answer = 0
left = 1
right = max(times) * n

while left <= right :
    mid = (left + right) // 2
    num = 0 # mid분동안 처리된 사람의 수
    for time in times :
        num += mid // time
        # 모든 심사관을 거치지 않고도 mid분동안 n명 이상 처리가 가능하면 break
        if num >= n : break
    # 심사한 사람 수가 심사 받아야 할 사람 수보다 적을 경우
    if num < n :
        left = mid + 1 # 시간을 늘린다
    else : # 심사한 사람 수가 심사 받아야 할 사람 수보다 많으면
        answer = mid
        right = mid - 1 # 시간을 줄인다
