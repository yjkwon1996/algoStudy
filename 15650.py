# 15650 N과 M (2)
# https://www.acmicpc.net/problem/15650

"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1. 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
2. 고른 수열은 오름차순이어야 한다.
"""
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 
# 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

# 백트래킹 2

N, M = map(int, input().split())

arr = [] 
def dfs() :
    if len(arr) == M :
        if (sorted(arr) == arr) :   # 정렬되었는지 확인(오름차순 정렬만 출력하기 위해서)
            print(' '.join(map(str, arr)))
        return
    
    for i in range(1, N+1) : 
        if i not in arr : 
            arr.append(i)
            dfs()
            arr.pop() 

dfs()


