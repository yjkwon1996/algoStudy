# 2019 카카오 개발자 겨울 인턴십
# 불량 사용자
# https://programmers.co.kr/learn/courses/30/lessons/64064


def solution(user_id, banned_id):
    answer = 0
    return answer






if __name__ == "__main__" :
    user_id1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id1 = ["fr*d*", "abc1**"] # 2
    user_id2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id2 = ["*rodo", "*rodo", "******"] # 2
    user_id3 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id3 = ["fr*d*", "*rodo", "******", "******"] # 3
    
    print(solution(user_id1, banned_id1))
    print(solution(user_id2, banned_id2))
    print(solution(user_id3, banned_id3))
    