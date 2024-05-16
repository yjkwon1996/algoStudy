from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for seq in skill_trees :

        q = deque(skill)
        flag = True
        for c in seq :
            if c not in q : # 스킬트리와 상관없는 스킬
                continue

            # 선행 스킬이 필요한 경우
            if c == q[0] : # 순서에 따라서 배울 수 있는 스킬인지
                q.popleft()
            else : # 못배우는 경우
                flag = False
                break

        if flag : # 모두 체크했는데 가능한 경우
            answer += 1
            
    return answer