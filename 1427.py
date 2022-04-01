# 1427 소트인사이드
# https://www.acmicpc.net/problem/1427

"""
정렬하려고 하는 수 N을 각 자리수별로 내림차순 정렬해서 출력하는 프로그렘
"""

N = str(input())
arr = []
for i in N :
    arr.append(i)
    
arr.sort(reverse=True)

for i in arr :
    print(i, end='')