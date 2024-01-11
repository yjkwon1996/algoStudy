# 소트. 크기가 N인 배열 A가 있다. 배열에 있는 모든 수는 서로 다르다. 이 배열을 소트할 때, 연속된 두 개의 원소만 교환할 수 있다. 그리고, 교환은 많아봐야 S번 할 수 있다. 이때, 소트한 결과가 사전순으로 가장 뒷서는 것을 출력한다.
#
# 입력
# 첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 각 원소가 차례대로 주어진다. 이 값은 1000000보다 작거나 같은 자연수이다. 마지막 줄에는 S가 주어진다. S는 1000000보다 작거나 같은 음이 아닌 정수이다.
#
# 출력
# 첫째 줄에 문제의 정답을 출력한다.

import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
S = int(input().rstrip())

for i in range(N) :
    if S <= 0 :
        break
    # 정렬하지 않은 값 중 최댓값을 찾아서
    maxNum = max(A[i:min(N, i+S+1)])
    idx = A.index(maxNum)

    # 하나씩 당겨오기
    for j in range(idx, i, -1) :
        tmp = A[j]
        A[j] = A[j-1]
        A[j-1] = tmp

    S -= (idx - i)

print(*A)







