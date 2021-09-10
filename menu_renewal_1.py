from itertools import combinations
from collections import Counter

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]	
# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]
# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]


"""
주문한 단품 메뉴들이 문자열 형식으로 담긴 배열 orders
스카피가 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course
스카피가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 오름차순 return
코스 요리는 최소 2개 이상
2명 이상의 손님으로부터 주문된 단품메뉴 조합 - 코스요리 메뉴 후보
요리 course[i]개 코스, 메뉴 구성을 찾아서 메뉴 구성을 return
"""
answer = []

for c in course : # [2, 3, 4]일 경우 2개, 3개, 4개짜리 조합 찾기
    tmp = []
    for o in orders :
        com = combinations(sorted(o), c) # orders에 대해 course개 만큼 조합
        tmp += com
    counter = Counter(tmp) # Counter모듈이용해서 조합된 주문 내역에 갯수를 count
    
    # 해당 조합을 주문한 사람이 1명이거나 해당 주문이 나온 적이 없다면 통과하고
    # 그렇지 않다면 현재 갯수에 해당하는 조합중 가장 많이 주문된 수를 가진 조합을 answer에 추가
    if len(counter) != 0 and max(counter.values()) != 1 :
        answer += [''.join(x) for x in counter if counter[x] == max(counter.values())]

answer = sorted(answer) # 이후 정렬해서 return