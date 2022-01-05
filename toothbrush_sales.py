# 2021 Dev-Matching: 웹 백엔드 개발자(상반기)
# 다단계 칫솔 판매
# https://programmers.co.kr/learn/courses/30/lessons/77486

# 칫솔 하나의 판매가는 100원, 판매원은 자신이 번 돈의 10%를 추천인에게 준다.
# 10%를 받은 추천인은 여기서 다시 10%를 상위 루트에 전달하고, 90%를 소유하는식으로 반복
# 최종 집계후 이익 배분 현황을 배열 형태로 return
# 최상위에는 민호(center)가 있다.
# 각 판매원의 이름을 담은 배열 enroll, 각 판매원을 다단계 조직에 참여시킨 다른 판매원의 이름을 담은 배열 referral
# 판매량 집계 데이터의 판매원 이름을 나열한 배열 seller, 판매량 집계 데이터의 판매 수량을 나열한 배열 amount
# 각 판매원이 득한 이익금을 나열한 배열을 return
# referral이 -인 경우, 마지막에 이익의 10%를 center에 전달

# seller가 얼마나 벌었는지 파악하고, 각 판매원의 상위 조직원에게 10%씩 전달?
# 트리 형태를 딕셔너리로 만들어서 부모노드로 돈을 넘겨주는 형식으로

def solution_fail(enroll, referral, seller, amount):
    answer = []
    
    people = { '-' : 'root'} # 사람 트리
    sell = {'-' : 0} # 판매액 트리
    
    # 트리 만들기
    for i in range(len(enroll)) :
        child = enroll[i]
        parent = referral[i]
        people[child] = parent
        sell[child] = 0
        
    # 판매액 구하기
    for i in range(len(seller)) :
        child = seller[i]
        parent = people[child]
        money = amount[i] * 100
        sell[child] += money
        # 부모 노드에게 10% 전달
        while True :
            quota = money // 10
            sell[child] -= quota
            sell[parent] += quota
            child = parent # 계산 후, 상위 노드로 이동해서 다시 계산
            parent = people[child]
            money = quota
            if parent == 'root' : break # 최상위 노드라면 반복 종료
    
    # 이후 sell 딕셔너리를 참고하여 각각의 판매액을 answer에 담고 리턴
    for person in enroll :
        answer.append(sell[person])
    
    return answer

# 테스트케이스 11, 12, 13에서 시간 초과 발생. 효율성에서 문제
# 좀 더 알아보도록 하자
# zip함수


import math
def solution(enroll, referral, seller, amount):
    answer = []
    parentTree = dict(zip(enroll, referral))
    answer = dict(zip(enroll, [0 for i in range(len(enroll))]))

    
    for i in range(len(seller)):
        earn = amount[i] * 100
        target = seller[i]

        while True :
            if earn < 10 : #10원 단위 이하라면 모두 받고 레퍼럴 종료
                answer[target] += earn
                break
            else : #10% 레퍼럴을 제외하고 받는다
                answer[target] += math.ceil(earn * 0.9)
                if parentTree[target] == "-": #상위가 없다면 종료
                    break
                earn = math.floor(earn*0.1)
                target = parentTree[target]
                    
    return list(answer.values()) 
        
        
    
    
    
    
    return answer




if __name__ == "__main__" :
    enroll1 = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    referral1 = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    seller1 = ["young", "john", "tod", "emily", "mary"]
    amount1 = [12, 4, 2, 5, 10]
    # result = [360, 958, 108, 0, 450, 18, 180, 1080]
    
    enroll2 = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    referral2 = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    seller2 = ["sam", "emily", "jaimie", "edward"]
    amount2 = [2, 3, 5, 4]
    # result = [0, 110, 378, 180, 270, 450, 0, 0]
    
    print(solution(enroll1, referral1, seller1, amount1))
    print(solution(enroll2, referral2, seller2, amount2))
