# 자물쇠와 열쇠

def solution(key, lock):
    """
    자물쇠 n x n, 열쇠 m x m
    열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 홈 부분에 딱 맞게 채우면 자물쇠가 열린다.
    자물쇠 영역을 벗어난 열쇠의 홈과 돌기는 자물쇠에 영향을 주지 않지만
    자물쇠 영역 내의 열쇠의 돌기와 자물쇠의 홈부분은 정확히 일치해야 하며
    열쇠의 돌기와 자물쇠의 돌기가 만나면 안되고, 자물쇠의 모든 홈을 채워 빈 홈이 없어야 한다.
    이 때, 열쇠로 자물쇠를 열 수 있으면 true, 없으면 false를 return
    """
    # 자물쇠 영역 외부는 상관이 없다 -> 자물쇠 영역을 확장시켜서, 특정 영역만 확인한다면
    # 자물쇠 배열의 끝부분이 열쇠 배열의 끝에만 닿을 수 있을 정도로 확장시켜서
    # 열쇠를 회전시키기도 해서 자물쇠의 모든 홈을 열쇠 한번의 사용으로 채울 수만 있다면 
    # true 반환, 그렇지 않으면 false 반환
    
    # 90도씩 4번, 360도까지 변환
    start = len(key) - 1 # 확장된 lock에서 기존의 lock가 시작되는 지점
    end = start + len(lock) # 확장된 lock에서 기존의 lock가 끝나는 지점
    
    for _ in range(0, 4) :
        for j in range(end) :
            for k in range(end) :
                if open_check(j, k, key, lock, start, end) :
                    return True
        key = rotate(key)
    return False
    
# 2차원 행렬 회전
# 90도 회전의 경우, 회전 후 x 인덱스 = 회전 이전의 y 인덱스
# 회전 후 y 인덱스 = (배열 크기 - 1 )-회전 이전의 x 인덱스
def rotate(arr) :
    n = len(arr)
    result = [[0] * n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            result[j][n-1-i] = arr[i][j]
    return result

# 열쇠로 자물쇠가 열리는지 확인
# 확장된 lock 배열을 이용하여, 각 좌표를 통해서 자물쇠의 홈을 열쇠로 채울 수 있는지 확인
def open_check(x, y, key, lock, start, end) :
    ex_size = len(lock) + start * 2 # 확장된 lock 배열의 크기
    ex_lock = [[0] * ex_size for _ in range(ex_size)]
    
    # 확장된 크기의 lock에 기존 lock의 정보 추가
    for i in range(start, end) :
        for j in range(start, end) :
            ex_lock[i][j] += lock[i-start][j-start]
    
    # key를 넣었을 때 자물쇠의 빈 홈이 채워지는지 확인. 돌기와 돌기가 만나거나 홈이 안채워지면 false
    for i in range(len(key)) :
        for j in range(len(key)) :
            ex_lock[x+i][y+j] += key[i][j]
            # 홈이 모두 맞아떨어지려면 값이 1이어야 함
            # 만약 ex_lock에 1이 아닌 값이 있으면 False return
            if ex_lock[i][j] != 1 :
                return False
    return True

if __name__ == "__main__" :
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))