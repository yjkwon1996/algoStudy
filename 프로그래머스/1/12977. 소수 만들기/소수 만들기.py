from itertools import combinations

def solution(nums):
    answer = 0

    comb = combinations(nums, 3)
    for c in comb :
        value = sum(c)
        flag = True
        for i in range(2, int(value**0.5)+1) :
            if value % i == 0 :
                flag = False
                break

        if flag :
            answer += 1

    return answer