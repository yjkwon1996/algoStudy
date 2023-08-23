# 10000 이하의 자연수로 이루어진 길이 N짜리 수열에서
# 연속된 수들의 부분합 중에 그 합이 S이상이 되는 것 중 가장 짧은 것의 길이를 구하기

import sys
input = sys.stdin.readline

N, S = map(int, input().rstrip().split())
num = list(map(int, input().rstrip().split()))

# 투포인터
left, right = 0, 0
length = sys.maxsize # 수열의 길이
value = 0 # 합

while True :

    # 합이 S를 넘으면 왼쪽을 이동시키면서 값을 확인
    if value >= S :
        length = min(length, right - left)
        value -= num[left]
        left += 1
    elif right == N:  # 마지막까지 탐색완료시. 위에서 왼쪽의 포인터를 이동 완료 후 break 해야하기 때문에 여기에 위치
        break
    else : # 합이 S를 못넘으면 오른쪽 포인터를 이동시키면서 더하기
        value += num[right]
        right += 1

if length == sys.maxsize : # 합이 S를 넘지 못했다면 길이는 maxsize이므로
    print(0) # 0 출력
else : # 합이 S를 넘은 경우, 그 중에서도 최솟값을 출력
    print(length)
