def solution(stones, k) :
    left = 1
    right = 200000000 # 최대 건널 수 있는 사람 수
    while left <= right :
        mid = (left + right) // 2 # 징검다리를 건널 수 있는 수
        blank = 0
        for i in stones : # stones의 각 원소 탐색
            if i - mid <= 0 : # 각 원소에서 징검다리를 건널 수 있는 수를 빼며 0 이하라면 blank += 1 
                blank += 1 # 건너야 할 디딤돌의 숫자가 0 이하면 blank += 1
            else : blank = 0 # mid 중 0보다 큰 원소가 있다면 blank를 0으로 초기화
            if blank >= k : break # blank와 k가 같거나 커진다면 반복 종료 후 right를 내린다.
        if blank >= k : # mid값보다 작은 구간이 연속적으로 k개 이상이면 (사용할 수 없는 돌이 k개 이상이면)
            right = mid - 1
        else : left = mid + 1 # mid값보다 작은 구간이 연속적으로 k개 미만이면(사용할 수 없는 돌이 k개 미만이면)
    

    return left