# 2750 수 정렬하기
# https://www.acmicpc.net/problem/2750

"""
N개의 수가 주어졌을 때 오름차순으로 정렬
"""
# 첫째 줄에 수의 개수 N이 주어지고
# 둘째 줄부터 N개의 줄에 수가 주어진다.
# 수는 중복되지 않으며 절댓값이 1000보다 작거나 같은 정수

"""
N = int(input())

arr = []
for i in range(N) :
    num = int(input())
    arr.append(num)

arr.sort()
for i in range(N) :
    print(arr[i])
    
"""

# 2751 수 정렬하기 2
# https://www.acmicpc.net/problem/2750

# 위와 동일하지만, 시간복잡도가 O(nlogn)으로 해결할 수 있다.
# N의 범위가 1000000으로 훨씬 크기 때문에 다른 방법이 필요하다. 병합정렬, 힙정렬, 내장함수...

# 내장함수

"""
import sys 

N = int(input())
arr = []
for i in range(N) :
    num = int(sys.stdin.readline()) # 입력 형식을 바꿔줌. Spyder에서는 오류 발생
    arr.append(num)

arr.sort()
for i in range(N) :
    print(arr[i])

"""

# 병합 정렬
# 앞 원소부터 분할&정복 방식으로 절반씩 합치면서 정렬

"""
def merge_sort(arr) :
    if len(arr) <= 1 :
        return arr
    
    # 재귀함수를 이용해서 마지막까지 분할
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    i, j, k = 0, 0, 0
    
    # 분할한 값들을 비교하고, 정렬(i와 j가 가리키는 값을 비교하여 작은 값을 k에)
    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            arr[k] = left[i]
            i += 1
        else :
            arr[k] = right[j]
            j += 1
        k += 1
        
    # 한쪽 리스트가 먼저 끝나면 나머지 값 비교
    if i == len(left) :
        while j < len(right) :
            arr[k] = right[j]
            j += 1
            k += 1
    elif j == len(right) :
        while i < len(left) :
            arr[k] = left[i]
            i += 1
            k += 1
    return arr

N = int(input())
arr = []
for i in range(N) :
    num = int(input())
    arr.append(num) 
       
arr = merge_sort(arr)

for i in arr :
    print(i)

"""

# 10989 수 정렬하기 3
# https://www.acmicpc.net/problem/10989

# 위와 동일하지만 N의 범위가 10,000,000 이하
# 수의 범위가 작다면 카운팅 정렬을 사용하여 더욱 빠르게 정렬할 수 있다
# 카운팅 정렬(계수 정렬)



