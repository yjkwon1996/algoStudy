# 15652 N과 M (4)
# https://www.acmicpc.net/problem/15652

"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1. 1부터 N까지 자연수 중에서 M개를 고른 수열
2. 같은 수를 여러 번 골라도 된다.
3. 고른 수열은 비내림차순이어야 한다.
    길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
"""
# 입력 : 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 
# 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

"""
# 시간초과
N, M = map(int, input().split())

arr = []

def dfs() :
    if len(arr) == M :
        if (sorted(arr) == arr) : # 비내림차순 정렬 확인
            print(' '.join(map(str, arr)))
        return
    for i in range(1, N+1) :
        arr.append(i)
        dfs()
        arr.pop()

dfs()

"""

N, M = map(int, input().split())

arr = []
def dfs(num) :
    if len(arr) == M :
        print(' '.join(map(str, arr)))
        return
    for i in range(num, N+1) :# num부터 시작해서 N+1까지 탐색
        arr.append(i)
        dfs(i) # 비내림차순 정렬 탐색이 된다.
        arr.pop()

dfs(1)

