def solution(arr1, arr2):
    """
    leve2_2를 간단하게 한 경우
    """
    answer = []

    for i in range(len(arr1)) :
        result = []
        for j in range(len(arr2[0])) :
            tmp = 0
            for k in range(len(arr2)) :
                tmp += arr1[i][k] * arr2[k][j]
            result.append(tmp)
        answer.append(result)
        
        
    return answer

# 이렇게 할 수도 있다.(zip(*) 이용)
# zip(*) -> 행과 열을 바꿔준다.
# sum(a*b for a, b in zip(A_row,B_col)) -> A의 행과 B의 열에 있는 원소를 각각 곱한다.
# for B_col in zip(*B) -> B_col은 B의 각 열을 순회하며 조회
# for A_row in A -> A의 각 행을 순회하며 조회
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

