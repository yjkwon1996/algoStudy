
arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
# arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
# arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]



"""
2차원 행렬 arr1, arr2
arr1에 arr2를 곱한 결과를 return
2차원 행렬곱
"""
answer = []
cnt = 0
for i in arr1 :
    res = []
    for tmp in range(len(i)) :
        idx = 0
        result = 0
        for j in arr2 :
            result += i[idx]*j[cnt]
            idx += 1
        res.append(result)
        if cnt != len(i)-1 :
            cnt += 1
        else : 
            cnt = 0
    answer.append(res)

print(answer)