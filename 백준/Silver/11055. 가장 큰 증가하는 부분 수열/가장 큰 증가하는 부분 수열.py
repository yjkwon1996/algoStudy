# 가장 큰 증가하는 부분 수열. 수열 A가 주어졌을 때, 그 수열의 증가하는 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.
#
# 예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가하는 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.
#
# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
#
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)
#
# 출력
# 첫째 줄에 수열 A의 합이 가장 큰 증가하는 부분 수열의 합을 출력한다.

import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))

dp = [0 for _ in range(N)] #
dp[0] = A[0]

for i in range(N) :
    for j in range(N) :
        if A[i] > A[j] : # 수열 [i]와 수열 [j]를 비교해서 [i]가 더 크다면
            dp[i] = max(dp[i], dp[j]+A[i]) # 현재 dp[i]값과 dp[j]+A[i]를 비교하여 더 큰값으로
        else : # 자기 자신의 값이나 지금까지의 dp값을 현재 dp값으로
            dp[i] = max(dp[i], A[i])

print(max(dp))



