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

def solution(stones, k):
    answer = 0
    
    st = dict()
    for i in range(len(stones)) :
        st[i] = stones[i]
    print(st)
    
    return answer


if __name__ == "__main__" :
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3 
    # result = 3
    
    print(solution(stones, k))