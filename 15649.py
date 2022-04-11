# 15649 N과 M (1)
# https://www.acmicpc.net/problem/15649

"""
자연수 N과 M이 주어졌을 때 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램 작성
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
"""
# 첫째 줄에 자연수 N과 M을 입력 (1 ≤ M ≤ N ≤ 8)
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 
# 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

# 백트래킹

N, M = map(int, input().split())

arr = [] # M개의 수열을 저장할 배열
def dfs() :
    if len(arr) == M : # 배열에 들어간 수열의 크기가 M개가 되었다면 출력
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1, N+1) : # 1부터 N까지
        if i not in arr : # 중복이 아니면 배열에 추가
            arr.append(i)
            dfs()
            arr.pop() # 다른 수열을 찾기 위해 하나를 빼준다.

dfs()

