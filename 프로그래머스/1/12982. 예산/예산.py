def solution(d, budget):
    answer = 0
    d = sorted(d)
    for i in d :
        answer += 1
        budget -= i
        if budget < 0 :
            answer -= 1
            break
        elif budget == 0:
            break
        
    return answer