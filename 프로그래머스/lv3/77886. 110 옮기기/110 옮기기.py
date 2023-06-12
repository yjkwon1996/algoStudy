def solution(s):
    answer = []
    # c = '110'
    
    # 어떤 문자열 x에 대해서 x를 최대한 사전 순으로 앞에 오도록
    # 최대한 작은 수가 되도록 하려면
    # 모든 110을 찾고, 뒷자리부터 확인하면서 0이 나오면 0 뒤에 모두 붙이기
    # 0이 없으면 전부 1이라는 뜻이므로, 앞에 모두 붙이기
    
    # 모든 110 찾기
    for i in s :
        cnt = 0 
        arr = []
        for x in i : # 각 배열을 잘라서 저장하면서 뒤에서부터 확인
            if len(arr) >= 2 and arr[-1] == '1' and arr[-2] == '1' and x == '0' : # 110 발견
                cnt += 1
                arr.pop()
                arr.pop()
            else :
                arr.append(x)
        
        char = ''.join(arr)
        # 110을 다 찾은 뒤
        # 뒤에서부터 체크해서 0이 나오면 그 뒤에 다 붙이고 0이 없으면 모두 앞에
        for idx in range(len(arr)-1, -1, -1) :
            if char[idx] == '0' :
                answer.append(char[:idx+1] + ('110' * cnt) + char[idx+1:])
                break
        else :
            answer.append('110' * cnt + char)
                
    return answer