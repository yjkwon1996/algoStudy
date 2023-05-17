def solution(s):
    answer = []
    
    # 문자열을 배열로
    s = s[2:-2]
    arr = s.split("},{")
    
    # 길이순 정렬
    arr.sort(key=len)
    
    # 앞에서부터 하나씩 넣으면 끝
    for i in arr :
        tmp = i.split(',')
        for j in tmp :
            if int(j) not in answer :
                answer.append(int(j))
    
    return answer