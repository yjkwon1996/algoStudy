def solution(s):
    answer = [0, 0]
    
    while s != "1" :
        answer[0] += 1
        length = len(s)
        s = s.replace('0', '') # 0 제거
        answer[1] += length - len(s) # 0을 없앤 문자의 길이
        s = str(bin(len(s)))[2:] # 이진 변환 후 문자열로
        print(s)
    
    return answer