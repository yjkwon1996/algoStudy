def solution(scores):
    answer = 1
    # 근무 태도 점수 / 동료 평가 점수
    # 어떤 사원이 다른 임의의 사원보다 두 점수가 모두 낮은 경우가 한 번이라도 있다면 인센티브 X
    # 그렇지 않은 사원에 대하여 두 점수의 합이 높은 순으로 인센티브 차등 지급. 합이 동일하면 동석차
    
    attitude, evaluation = scores[0]
    score = attitude + evaluation
    
    # 태도 점수에 대해서는 내림차순, 평가 점수에 대해서는 오름차순 정렬
    scores.sort(key=lambda x: (-x[0], x[1]))
    beforeMax = 0 # 앞에 나온 어떤 학생의 합
    
    for a, e in scores :
        if attitude < a and evaluation < e : # 완호가 인센티브를 받지 못하는 경우
            return -1
        
        if e >= beforeMax : # 석차 계산
            beforeMax = e
            if a + e > score :
                answer += 1
    
    return answer