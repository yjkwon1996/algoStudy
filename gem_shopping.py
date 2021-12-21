# 2020 카카오 인턴십
# 보석 쇼핑
# https://programmers.co.kr/learn/courses/30/lessons/67258

# 정확성, 효율성 테스트
# 특정 범위를 모두 구매해야 함. 중간에 빠질 수 없음
# 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매하기
# ex) 3 4 5 6 7 에 루비 다이아 다이아 에메랄드 사파이어가 있으면, 다이아가 2번 중복되더라도 모두 구매해야 함
# 진열대 번호 순서대로 보석들의 이름이 저장된 배열 gems
# 모든 보석을 하나 이상 보함하는 가장 짧은 구간을 찾아서 return. [시작번호, 끝번호] 형태로 return

# gems 배열 내에서, 중복을 제외하고 모든 요소들을 한번씩은 구매해야 한다.
# 중복 제거한 set을 이용해서 구매해야 할 요소들의 목록을 만들고, 이것을 활용하여 계산


# 효율성에서 통과 실패
def solution_fail(gems):
    answer = []
    arr = list(set(gems)) # 포함되어야 하는 요소들을 저장
    arr_set = set()
    
    start = 0
    end = len(gems) - 1
    
    
    for i in range(len(gems)) : # 순회를 통해 짧은 구간을 갱신
        for j in range(i, len(gems)) :
            arr_set.add(gems[j])
            if len(arr_set) == len(set(gems)) and end - start > j - i :
                start = i
                end = j
                break
        arr_set.clear()
    answer.append(start+1)
    answer.append(end+1)

    
    return answer



# 효율성 통과를 위한 코드
# 투 포인터 알고리즘
# 리스트에 순차적으로 접근해야 할 때 두 개의 점 위치를 기록하면서 처리하는 알고리즘
# start와 end, 두개의 포인트를 사용한다.



def solution(gems):
    answer = []

    
    return answer


if __name__ == "__main__" :
    gems1 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"] # [3, 7]
    gems2 = ["AA", "AB", "AC", "AA", "AC"] # [1, 3]
    gems3 = ["XYZ", "XYZ", "XYZ"] # [1, 1]
    gems4 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"] # [1, 5]
    
    print(solution(gems1))
    print(solution(gems2))
    print(solution(gems3))
    print(solution(gems4))
    