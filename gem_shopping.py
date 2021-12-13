# 2020 카카오 인턴십
# 보석 쇼핑
# https://programmers.co.kr/learn/courses/30/lessons/67258

# 정확성, 효율성 테스트
# 특정 범위를 모두 구매해야 함. 중간에 빠질 수 없음
# 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매하기
# ex) 3 4 5 6 7 에 루비 다이아 다이아 에메랄드 사파이어가 있으면, 다이아가 2번 중복되더라도 모두 구매해야 함
# 진열대 번호 순서대로 보석들의 이름이 저장된 배열 gems
# 모든 보석을 하나 이상 보함하는 가장 짧은 구간을 찾아서 return. [시작번호, 끝번호] 형태로 return


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
    