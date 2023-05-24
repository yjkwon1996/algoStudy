import sys
def solution(a):
    answer = 0
    
    # 선택한 풍선에서 왼쪽 또는 오른쪽에서 보다 작은 번호가 두번 이상 나오면 X
    leftMin = [sys.maxsize for _ in range(len(a))]
    rightMin = [sys.maxsize for _ in range(len(a))]
    leftMin[0] = a[0]
    rightMin[-1] = a[-1]
    
    for i in range(1, len(a)) : # 왼쪽에서부터 최솟값 저장
        leftMin[i] = min(leftMin[i-1], a[i])
    
    for i in range(len(a)-2, -1, -1) : # 오른쪽에서부터 최솟값 저장
        rightMin[i] = min(rightMin[i+1], a[i])
        
    # a의 모든 요소를 확인하면서 a[i]가 leftMin[i], rightMin[i] 두 수보다 크면 남기기 X
    for i in range(len(a)) :
        if a[i]>leftMin[i] and a[i]>rightMin[i] :
            continue
        answer += 1
    
    
    return answer