L = int(input()) # 집합의 크기
arr = list(map(int, input().split()))
n = int(input())

arr.append(0) # 0부터
arr.sort() # 집합 정렬

start = 0
for i in range(len(arr)-1) :
    if arr[i] == n or arr[i+1] == n : # 집합의 수가 이미 있다면 0
        start = 0
        break
    elif arr[i] < n and n < arr[i+1]: # 집합의 범위를 찾아서 그 구간의 범위를 계산해주기
        start = (n - arr[i]) * (arr[i+1] - n) - 1 # 앞 * 뒤 - 1(중복 제거)
        break
    
print(start)