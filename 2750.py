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

# 위와 동일하지만 N의 범위가 10,000,000 이하. 중복 가능.
# 수의 범위가 작다면 카운팅 정렬을 사용하여 더욱 빠르게 정렬할 수 있다
# 카운팅 정렬(계수 정렬)
# 메모리 초과

"""
N = int(input())
arr = []
for i in range(N) :
    num = int(input())
    arr.append(num) 
cnt = [0] * (max(arr) + 1) # 숫자 i가 배열에 몇 개 존재하는지(중복 허용)

for i in arr :
    cnt[i] += 1

for i in range(1, len(cnt)) : # 누적합 방식으로 갱신
    cnt[i] += cnt[i-1]

answer = [0] * len(arr) # arr의 각 원소를 정렬된 위치에 삽입

# arr의 원소값을 cnt의 인덱스값으로 사용해 가져온 후 다시 answer의 인덱스 값으로 사용하여 arr의 원소로 저장
# 이후, cnt[arr[i]]의 값 1 감소
for i in arr :
    idx = cnt[i]
    answer[idx-1] = i
    cnt[i] -= 1

print(answer)


"""

# 딕셔너리를 이용해서도 가능한 카운팅 정렬

"""

N = int(input())
arr = []
for i in range(N) :
    num = int(input())
    arr.append(num) 

cnt_dict = {}

for i in arr :
    if i in cnt_dict :
        cnt_dict[i] += 1
    else :
        cnt_dict[i] = 1

answer = []

for i in range(max(arr) + 1) :
    while i in cnt_dict and cnt_dict[i] != 0 :
        answer.append(i)
        cnt_dict[i] -= 1

print(answer)
    
"""

# 문제 풀이

import sys

N = int(sys.stdin.readline())
arr = [0] * 10001

# append가 아닌 다른 방식 이용. 미리 arr의 크기를 지정해준다(수 크기는 10000이하)
# 각 배열의 인덱스 값을 이용하여 인덱스 값에서 몇 수만큼 있는지

for i in range(N) :
    arr[int(sys.stdin.readline())] += 1 
    
for i in range(10001) :
    if arr[i] != 0 :
        for j in range(arr[i]) :
            print(i)


