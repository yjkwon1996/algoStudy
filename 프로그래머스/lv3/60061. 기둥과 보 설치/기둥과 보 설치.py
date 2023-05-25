# 구조물이 조건에 충족하는지
def check(arr, n) :
    for x, y, a in arr :
        if a == 0 : # 기둥이면 바닥 or 보의 한쪽 끝 or 다른 기둥 위 
            # 기둥을 설치할 공간도 있어야함
            if y<n :
                if y==0 or [x-1, y, 1] in arr or [x, y, 1] in arr or [x, y-1, 0] in arr :
                    continue
            return False # 하나라도 만족을 못하면 false
        elif a == 1 : # 보면 한쪽 끝 부분이 기둥 위 or 양쪽 끝 부분이 다른 보와 동시에 연결
            # 보를 설치할 공간도 있어야함
            if x<n :
                if [x, y-1, 0] in arr or [x+1, y-1, 0] in arr or ([x-1, y, 1] in arr and [x+1, y, 1] in arr) :
                    continue
            return False
    return True
        

def solution(n, build_frame):
    answer = []
    
    # 벽면의 크기 n.
    # build_frame : [x, y, a, b] -> (x, y) : 기둥, 보를 설치 또는 삭제할 교차점의 좌표
    # a : 설치 또는 삭제할 구조물의 종류(0 기둥, 1 보)
    # b : 0 삭제, 1 설치
    
    # 리턴 값 : [x, y a] . (x, y) : 좌표, a : 0 기둥, 1 보
    # x좌표 기준 오름차순 정렬, y좌표 오름차순 정렬, 기둥이 보보다 앞에 오도록
    
    for x, y, a, b in build_frame :
        if b == 0 : # 삭제
            # 조건 확인 후 삭제
            answer.remove([x, y, a])
            if not check(answer, n) :
                answer.append([x, y, a])
        else : # 설치
            # 조건 확인 후 설치
            answer.append([x, y, a]) 
            if not check(answer, n) :
                answer.remove([x, y, a])

    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    print(answer)

    return answer