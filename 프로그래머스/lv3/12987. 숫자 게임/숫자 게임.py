def solution(A, B):
    answer = 0
    
    # 정렬해서 순서대로 비교
    A.sort()
    B.sort()
    
    # 앞에서부터 차례대로 크기 비교
    for i in range(len(A)) :
        for j in range(len(B)) :
            if A[i] < B[j] : # B가 더 큰 경우를 찾으면 그 값 제거 후 answer 추가
                answer += 1
                B.remove(B[j])
                break
            
    
    return answer