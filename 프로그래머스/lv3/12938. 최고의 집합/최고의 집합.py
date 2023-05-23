def solution(n, s):
    answer = []
    
    # 표준편차가 가장 적은 수로 만들어야 함
    # ex) n=3, s=10 -> 3 * 3 * 4 이 나오도록
    init = s // n
    if init == 0 : # 합이 n인 집합을 못만듬
        answer = [-1]
        return answer
    
    mod = s % n # +1을 해줘야 하는 값의 갯수
    
    for i in range(n-mod) :
        answer.append(init)
    for i in range(mod) :
        answer.append(init+1)
    
    # 이렇게도 가능
    # return [init for _ in range(n-mod)] + [(init+1) for _ in range(mod)]
    
    return answer