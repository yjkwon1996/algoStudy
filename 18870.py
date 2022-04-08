# 18870 좌표압축
# https://www.acmicpc.net/problem/18870
# 만약 정확한 값이 필요 없고 값의 대소 관계만 필요하다면, 모든 수를 0 이상 N 미만의 수로 바꿀 수 있습니다.

"""
수직선 위에 N개의 좌표 X1, X2, X3, ... XN가 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
각 X에 좌표 압축을 적용한 결과 X'i를 출력
"""
# 첫째 줄에는 N이 주어진다.
# 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, X3, ... XN이 주어진다.
# X'i ... 를 공백 한 칸으로 구분해서 출력

# 각 좌표 값의 순위값

"""
# 시간 초과 발생

N = int(input())

arr = list(map(int, input().split())) # 각 좌표를 입력받고 배열에 저장
rank_arr = sorted(list(set(arr))) # 각 좌표들에서 중복을 제거하고 정렬

for i in arr :
    print(rank_arr.index(i), end=' ') # 정렬한 값들의 index를 순위로 이용하여 좌표 압축

"""

"""
# 그래도 시간초과
import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split())) # 각 좌표를 입력받고 배열에 저장
rank_arr = sorted(list(set(arr))) # 각 좌표들에서 중복을 제거하고 정렬

for i in arr :
    print(rank_arr.index(i), end=' ') # 정렬한 값들의 index를 순위로 이용하여 좌표 압축

"""


N = int(input())

arr = list(map(int, input().split())) # 각 좌표를 입력받고 배열에 저장
rank_arr = sorted(list(set(arr))) # 각 좌표들에서 중복을 제거하고 정렬

rank_dict = {rank_arr[i] : i for i in range(len(rank_arr))} # dict를 이용하여 시간 복잡도 줄이기
for i in arr :
    print(rank_dict[i], end=' ') 


