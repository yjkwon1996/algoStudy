

msg = "KAKAO"
# msg = "TOBEORNOTTOBEORTOBEORNOT"
# msg = "ABABABABABABABAB"

"""
LZW 압축
1. 길이가 1인 모든 단어를 포함하도록 사전 초기화
2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다
3. w에 해당하는 사전의 객인 번호를 출력하고, 입력에서 w를 제거
4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록
2로 돌아감
영문 대문자로 이뤄진 문자열 msg 
msg을 압축한 후의 사전 색인 번호를 배열로 return
"""

answer = []
# A ~ Z 까지 dict 형식으로 A:1, B:2 ~ Y:25, Z:26
dictionary = dict()
for i in range(ord('A'), ord('Z') + 1) :
    dictionary[chr(i)] = i - 64

idx = 0
cnt = 0
length = 26
while True :
    cnt += 1
    if msg[idx:idx+cnt] not in dictionary : # 사전에 없는 문자를 새로 등록
        length += 1
        dictionary[msg[idx:idx+cnt]] = length
        answer.append(dictionary[msg[idx:idx+cnt-1]])
        idx = idx + cnt - 1
        cnt = 0
    else : # 사전에 있으면
        if idx+cnt == len(msg) :
            answer.append(dictionary[msg[idx:idx+cnt]])
            break
print(answer, dictionary)

