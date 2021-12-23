# # 2021 KAKAO BLIND RECRUITMENT
# 합승 택시 요금
# https://programmers.co.kr/learn/courses/30/lessons/72413

# 정확성과 효율성 테스트가 있음
# 

def solution(n, s, a, b, fares):
    answer = 0
    
    
    return answer




if __name__ == "__main__" :
    n1, s1, a1, b1 = 6, 4, 6, 2
    fares1 = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    # result = 82
    n2, s2, a2, b2 = 7, 3, 4, 1
    fares2 = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
    # result = 14
    n3, s3, a3, b3 = 6, 4, 5, 6
    fares3 = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
    #result = 18
    
    print(solution(n1, s1, a1, b1, fares1))
    print(solution(n2, s2, a2, b2, fares2))
    print(solution(n3, s3, a3, b3, fares3))