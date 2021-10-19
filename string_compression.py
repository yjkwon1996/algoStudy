def solution(s):
    """
    문자열 압축
    ex) aabbaccc -> 2a2ba3c(반복이 1번인 경우 1은 생략)
    ex) ababcdcdababcdcd -> 2ab2cd2ab2cd(2개 단위로 잘라서 압축)
    ex) abcabcdede -> 2개단위 압축시 : abcabc2de, 3개단위 압축시 : 2abcdede. 3개가 가장 짧음
    압축할 문자열 s가 매개변수로 주어질 때 위의 방법으로 1개 이상 단위로 문자열을 잘라 압축하여
    표현한 문자열 중 가장 짧은 것의 길이를 return
    """
    # 반복되는 문자열을 찾고, 카운트를 계산.
    # 제일 앞에서부터 정해진 길이만큼 잘라야 함
    # 1개 단위 압축, 2개단위압축, 3개단위 압축...
    # 이후, 각 단위를 비교하여 가장 짧은 경우를 찾아서 return하면 된
    answer = 0
    
    char_arr = []
    if len(s) == 1 : # 문자열 길이가 1이면 1 return
        return 1
    
        
    # 문자열을 자르는 단위. 2로 나눠 문자열 길이를 넘어가는 비교를 안하도록 한다.
    # ex) 문자열의 길이가 10이면 최대 반복하는 단위는 5
    for j in range(1, (len(s) // 2) + 1) : 
        tmp_str = s[:j]
        cnt = 1
        char = ""
        for i in range(j, len(s), j) : # 문자열만큼, 문자열을 건너띄면서 확
            if s[i:i+j] == tmp_str :
                cnt += 1
            else : 
                if cnt == 1 :
                    char += tmp_str
                else :
                    char += str(cnt)+tmp_str
                tmp_str = s[i:i+j]
                cnt = 1
        if cnt == 1 :
            char += tmp_str
        else :
            char += str(cnt)+tmp_str
            
        char_arr.append(len(char))
        answer = min(char_arr)
    return answer


if __name__ == "__main__" :
   s1 = "aabbaccc"
   s2 = "ababcdcdababcdcd"
   s3 = "abcabcdede"
   s4 = "abcabcabcabcdededededede"
   s5 = "xababcdcdababcdcd"
   
   print(solution(s1)) # 7
   print(solution(s2)) # 9 
   print(solution(s3)) # 8
   print(solution(s4)) # 14
   print(solution(s5)) # 17