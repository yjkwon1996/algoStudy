# 2019 카카오 개발자 겨울 인턴십
# 불량 사용자
# https://programmers.co.kr/learn/courses/30/lessons/64064

"""
불량 사용자라는 이름으로 목록을 따로 모아서 당첨 처리시 제외하도록
개인정보 보호를 위해 가리고자 하는 문자 하나에 *, 아이디당 최소 하나 이상의 *
이벤트 응모자 아이디 목록이 담긴 배열 user_id,
불량 사용자 아이디 목록이 담긴 배열 banned_id
당첨에서 제외되어야 할 제재 아이디 목록은 몇가지 경우의 수가 가능한지 return
예시 1에서
fr*d* -> frodo, fradi 두가지 경우의 수
abd1** -> abc123 한가지 경우의 수
2 * 1 = 2. 두가지 경우의 수가 가능하다.
"""

# 경우의 수를 어떻게 계산하는가?
# 글자수를 고려해야 한다.
# *의 개수, 위치를 고려해서 banned_id에 있는 아이디와 user_id에 있는 아이디가 가능한 경우를 찾는다.
# 문자열 비교에서 중복을 피해야 한다. frodo를 fr*d*에서 썼으면 *rodo에서 다시 사용하기는 불가능 -> set : 중복제거
# set과 순열을 이용하여 banned_id의 가능한 조합에서 user_id를 찾고 경우의 수를 계산하면 된다?
# 순열 permutation, 조합 combination. 중복 제거한 집합 set
# 

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
    