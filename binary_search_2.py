distance = 25
rocks = [2, 14, 11, 21, 17]	
n = 2


"""
출발지점부터 도착지점까지의 거리 distance, 바위들이 있는 위치를 담은 배열 rocks
제거할 바위의 수 n. 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중 max를 return
바위 사이의 거리의 최솟값을 구하고 그 중 최댓값을 찾는다.
"""
answer = 0
left = 1
right = distance
rock = sorted(rocks)
rock.append(distance) # 도착지점까지의 거리도 계산하기 위해 배열에 추가
while left <= right :
    mid = (left + right) // 2
    # 거리가 최소인 값이 mid 이하면 제거
    min_value = 1000000001 # 각 mid에서 최소값
    position = 0 # 현재 위치
    count = 0 # 바위를 제거한 개수
    
    for i in rock :
        diff = abs(i - position) # 현재 위치와 바위의 거리
        if diff < mid : # diff가 mid 이하면 바위 제거
            count += 1
        else : # diff가 mid보다 크면 
            position = i # 현재 위치를 바위로 이동
            min_value = min(min_value, diff) # 그 mid 값에서 최소거리인지
            
    # 바위를 n보다 많이 제거했다면
    if count > n :
        right = mid - 1 # mid값을 작게 해서, 더 적은 바위를 제거하도록 한다
    else : # 바위를 n보다 적게 제거했거나 알맞다면
        answer = min_value
        left = mid + 1 # mid값을 크게 해서, 더 많은 바위를 제거하도록 한다

