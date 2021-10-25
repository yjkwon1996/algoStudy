# 2019 KAKAO BLIND RECRUITMENT 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    answer = []
    """
    채팅방에 누군가 들어오면 "[닉네임]님이 들어왔습니다."
    채팅방에 누군가 나간다면 "[닉네임]님이 나갔습니다."
    중복 닉네임을 허용. 
    record에는 [입장(퇴장) uid (닉네임, 닉네임은 퇴장시에는 표시안됨)]
    A로 입장 후 B로 닉네임을 변경했다면 : A님이 들어왔습니다가 아닌 B님이 들어왔습니다로 표시
    A가 퇴장 후 B 닉네임으로 들어왔다면 : 이전에 입장한 기록도 B님이 들어왔습니다로 표시
    """
    log = dict()
    
    # record를 뒤에서부터 순회하면서 enter, change가 나온다면 같은 uid의 다른 모든 행동에서의 이름을 변경
    visited = []
    for i in record[::-1] :
        tmp = i.split()
        
        if tmp[0] == 'Change' or tmp[0] == 'Enter' :
            if tmp[1] not in visited : # 마지막 행동으로 enter, change를 했다면
                visited.append(tmp[1]) 
                # uid와 닉네임을 dict 형태로
                log[tmp[1]] = tmp[2]
            else : continue
        
    
    # change는 출력하지 않아도 된다.
    for i in record :
        tmp = i.split()
        value = log.get(tmp[1])
        if tmp[0] == 'Enter' : 
            char = value + "님이 들어왔습니다."
            answer.append(char)
        if tmp[0] == "Leave" :
            char = value + "님이 나갔습니다."
            answer.append(char)
            

    return answer

if __name__ == "__main__" :
   record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
   print(solution(record)) 
   # ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
   