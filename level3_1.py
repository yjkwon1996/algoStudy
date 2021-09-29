"""
n = 11
stations = [4, 11]
w = 1
# answer = 3
"""

n = 16
stations = [9]
w = 2
# answer = 3


"""
N개의 아파트 일렬로
5G 기지국은 범위가 좁다.
기지국을 최소로 설치하면서 모든 아파트에 전파를 전달하려면
n개의 아파트 개수, 현재 기지국이 설치된 아파트의 번호가 담긴 1차원 배열 stations,
전파의 도달 거리 w
모든 아파트에 전파를 전달하기 위해 증설해야 할 기지국의 개수의 최솟값을 return
"""
answer = 0
# 뒤에서부터 거리를 계산하면서 설치
# 설치가 안돼 있는 곳을 계산

# 전파 범위
ran = w*2+1

# dict 형태로 전파가 도달하는지 확인하는 형태
arr = dict()
for i in range(n+1) :
    arr[i] = 0
arr[0] = 1 # 0번은 제외

for i in stations :     # 전파가 도달하는 곳
    for j in range(w+1) :
        arr[i-j] = 1
        arr[i+j] = 1
# 기존의 아파트 범위를 초과한 부분 제거
for i in range(1, len(arr)-n) :
    arr.pop(n+i)

idx = 0
count = 0 # 몇 칸 동안 전파가 도달하지 않는지
for idx in range(n+1) :
    if arr[idx] == 0 :
        count += 1
    else : # 전파가 도달하는 구간을 만난 경우 기지국 설치
        while count > 0 :
            count -= ran
            answer += 1
        count = 0

# 마지막에 전파가 닿지 못했다면
while count > 0 :
    count -= ran
    answer += 1

    
            
    
print(arr)

print(answer)

"""
from math import ceil

"""
# N개의 아파트 일렬로
# 5G 기지국은 범위가 좁다.
# 기지국을 최소로 설치하면서 모든 아파트에 전파를 전달하려면
# n개의 아파트 개수, 현재 기지국이 설치된 아파트의 번호가 담긴 1차원 배열 stations,
# 전파의 도달 거리 w
# 모든 아파트에 전파를 전달하기 위해 증설해야 할 기지국의 개수의 최솟값을 return
"""
answer = 0
# 전파 범위
ran = w*2+1

# 기지국의 수를 최소로 해야 하므로 전파 범위로 나누고 정수로 올림한 수만큼 배치하면 최솟값
idx = 1
for i in stations : # 기지국을 순회하며, 기지국 왼쪽 범위의 합 계산
    answer += max(ceil((i-w-idx) / ran), 0)
    idx = i + w + 1

if n >= idx : # 순회가 끝난 이후 오른쪽 범위가 남으면 여기도 더해줌
    answer += ceil((n-idx+1) / ran)
    
"""
