# 접두사. 접두사X 집합이란 집합의 어떤 한 단어가, 다른 단어의 접두어가 되지 않는 집합이다.
# 예를 들어, {hello}, {hello, goodbye, giant, hi}, 비어있는 집합은 모두 접두사X 집합이다. 하지만, {hello, hell}, {giant, gig, g}는 접두사X 집합이 아니다.
# 단어 N개로 이루어진 집합이 주어질 때, 접두사X 집합인 부분집합의 최대 크기를 출력하시오.
# 입력
# 첫째 줄에 단어의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 단어가 주어진다.
# 단어는 알파벳 소문자로만 이루어져 있고, 길이는 최대 50이다. 집합에는 같은 단어가 두 번 이상 있을 수 있다.
# 출력
# 첫째 줄에 문제의 정답을 출력한다.

import sys
input = sys.stdin.readline

N = int(input().rstrip())
S = [input().rstrip() for _ in range(N)]

# 문자열이 짧은 것부터 앞에서부터 확인
S.sort(key=len)
answer = 0

for i in range(N) : # 각각의 문자열을 대상으로 해서
    flag = False
    for j in range(i+1, N) : # 각각 접두사인지 확인
        if S[i] == S[j][:len(S[i])] :
            flag = True
            break
    if not flag :
        answer += 1

print(answer)




