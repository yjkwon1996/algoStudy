# 2018 KAKAO BLIND RECRUITMENT
# 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677

"""
자카드 유사도 : 집합 간의 유사도를 검사하는 여러 방법 중 하나.
두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의됨.
EX) A = {1, 2, 3}, B = {2, 3, 4} 일 때 교집합은 {2, 3}, 합집합은 {1, 2, 3, 4}
J(A, B) = 2 / 4 = 0.5. 둘 모두가 공집합일때의 유사도는 1
자카드 유사도는 중복을 허용. A = {1, 1, 2, 2, 3}, B = {1, 2, 2, 4, 5} 일 때
교집합은 {1, 2, 2}, 합집합은 {1, 1, 2, 2, 3, 4, 5}. J(A, B) = 3 / 7 = 0.42가 된다.
이를 이용하여 문자열 사이의 유사도 계산에 이용 가능
FRANCE -> {FR, RA, AN, NC, CE}, FRENCH -> {FR, RE, EN, NC, CH}
교집합은 {FR, NC}, 합집합은 {FR, RA, AN, NC, CE, RE, EN, CH}
J("FRANCE", "FRENCH") = 2 / 8 = 0.25
대소문자는 관계 없음. 대문자 = 소문자 동일 취급
유사도의 값에서 65536을 곱한 수에서 소수점 아래를 버리고 정수부만 RETURN
"""

def solution(str1, str2):
    answer = 0
    
    # 모든 알파벳을 대문자로 변환
    str1, str2 = str1.upper(), str2.upper()
   
    # 두글자씩 끊어서 다중집합 원소로 만든다. 이 때, 알파벳 이외의 문자는 제외한다.
    # ex) ab+ -> ab. b+은 버린다.
    str1_arr = []
    str2_arr = []
    for i in range(len(str1)-1) : # 문자열을 두 글자로. 알파벳 이외의 문자 제외
        if str1[i:i+2].isalpha() == True:
            str1_arr.append(str1[i:i+2])
    for i in range(len(str2)-1) :
        if str2[i:i+2].isalpha() == True:
            str2_arr.append(str2[i:i+2])
        
    # str1_arr 집합과 str2_arr 집합의 교집합, 합집합을 찾는다.
    # 교집합의 개수 구하기. 크기가 작은 리스트에 있는 원소가 크기가 큰 리스트에 있으면 교집합 수 +1
    intersection = 0
    for i in min(str1_arr, str2_arr) : # str1_arr과 str2_arr 집합 중 크기가 작은 리스트에서 i
        if max(str1_arr, str2_arr).count(i) != 0 : # 그 i값과 동일한 문자의 count가 0이 아니면(1 이상이면)
            intersection += 1 # intersetion(교집합)의 개수 1 증
    
    # 합집합의 개수 구하기
    # 합집합 = 집합 + 집합 - 교집합
    union = len(str1_arr) + len(str2_arr) - intersection
    
    # 공집합인 경우 -> 유사도의 값은 1
    if union == 0 : # str1과 str2의 합집합이 0 == 공집합
        return 65536
    
    answer = int(intersection/union * 65536)
     
    return answer


if __name__ == "__main__" :
    str1_1, str2_1 = 'FRANCE', 'french'
    str1_2, str2_2 = 'handshake', 'shake hands'
    str1_3, str2_3 = 'aa1+aa2', 'AAAA12'
    str1_4, str2_4 = 'E=M*C^2', 'e=m*c^2'
    print(solution(str1_1, str2_1))
    print(solution(str1_2, str2_2))
    print(solution(str1_3, str2_3))
    print(solution(str1_4, str2_4))