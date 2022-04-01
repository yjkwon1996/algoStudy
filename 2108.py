# 2108 통계학
# https://www.acmicpc.net/problem/2108


"""
N은 홀수라고 가정.
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때 네 가지 기본 통계값을 구하는 프로그램을 작성
"""
# 첫째 줄에 수의 개수 N(1 <= N <= 500000)이 주어진다.
# 그 다음 N개의 줄에는 정수들이 주어진다.
# 입력되는 정수의 절댓값은 4000을 넘지 않는다.
# 산술평균, 중앙값, 최빈값, 범위를 줄단위로 바꾸면서 출력한다.
# 산술평균은 소수점 이하 첫째 자리에서 반올림한 값을 출력
# 최빈값이 여러개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력

from collections import Counter
import sys

N = int(input())
arr = []
for i in range(N) :
    arr.append(int(input()))
    # arr.append(int(sys.stdin.readline())) # 백준 시간초과 문제 해결
    
# 산술평균
print(round(sum(arr)/N)) 

# 중앙값
arr.sort()
print(arr[N//2])

# 최빈값
freq = Counter(arr).most_common(2)
if len(freq) > 1:
    if freq[0][1] == freq[1][1] : # 최빈값이 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력
        print(freq[1][0])
    else :
        print(freq[0][0])
else :
    print(freq[0][0])

# 범위
print(max(arr) - min(arr))
