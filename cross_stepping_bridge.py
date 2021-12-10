# 2019 카카오 개발자 겨울 인턴십
# 징검다리 건너기
# https://programmers.co.kr/learn/courses/30/lessons/64062

# 정확성, 효율성 테스트
# 일렬로 놓여있는 징검다리. 각 징검다리의 디딤돌에는 숫자가 적혀 있으며 한번 밟을 때마다 1씩 감소
# 디딤돌의 숫자가 0이되면 밟을 수 없음. 이 떄는 그 다음 디딤돌로 한번에 여러칸을 건너뛸 수 있음
# 단, 다음으로 밟을 수 있는 디딤돌이 여러개인 경우 무조건 가장 가까운 디딤돌로만 건너뛸 수 있음
# 한 번에 한명씩 징검다리를 건너며 디딤돌에 적힌 숫자가 담긴 배열 stones와 디딤돌의 최대 칸 수 k
# 최대 몇 명까지 징검다리를 건널 수 있는지 계산하여 return

# 한 번에 건너뛸 수 있는 디딤돌의 수는 k.
# k=3 일 때, 네칸을 건너뛸 수 없고 계산을 종료하여 answer값을 return
# dict : key는 몇번째 디딤돌인지, value는 디딤돌의 숫자로 계산하면 될듯?
# 아니면 dict 필요 없을지도... -> 필요 없을듯?
# 효율성 탐색을 통과하기 위해서 이분탐색 수행(left, right)


# 이렇게 하면 정확도는 통과하지만 효율성에서 떨어짐
def solution_1(stones, k):
    answer = 0
    
    while True :
        blank = 0 # 건너뛰는 횟수
        answer += 1
        for i in range(len(stones)) :
            if stones[i] == 0 : # 건너야 할 디딤돌의 숫자가 0이면
                continue
            else : stones[i] -= 1 # 건너야 할 디딤돌의 숫자가 1 이상이면 건너서 숫자를 -1
        for i in stones :
            if i == 0 : # 건너야 할 디딤돌의 숫자가 0이면
                blank += 1
                if blank == k : # 건너뛰는 횟수가 k가 된다면 탐색 종료
                    return answer
            else : blank = 0 # 건너야 할 디딤돌의 숫자가 0이 아니라면 blank 초기화
        
    return answer

# 따라서 효율성 해결을 위해 이분탐색 수행
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




if __name__ == "__main__" :
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3 
    # result = 3
    
    print(solution(stones, k))