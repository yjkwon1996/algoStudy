# 제곱ㄴㄴ수. 어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 그 수를 제곱ㄴㄴ수라고 한다. 제곱수는 정수의 제곱이다.
# min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수가 몇 개 있는지 출력한다.
# 첫째 줄에 두 정수 min과 max가 주어진다.
# 첫째 줄에 min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수의 개수를 출력한다.

import sys
import math
input = sys.stdin.readline

minNum, maxNum = map(int, input().rstrip().split())

answer = maxNum - minNum + 1
square = [False for _ in range(maxNum - minNum + 1)] # 제곱수 체크. 10, 100인 경우 10 ~ 100. 91개의 경우만 체크
idx = 2

while idx*idx <= maxNum : # 제곱수를 다 계산할 필요 없음
    squareNum = idx*idx # 제곱수

    if minNum % squareNum == 0 : # 소수점 처리. 제곱수니까
        mod = 0
    else :
        mod = 1

    multiple = minNum // squareNum + mod # 제곱수로 나눈 몫 -> 배수. 큰 수에서 시작해서 작은 수로 제곱수를 계산

    while squareNum * multiple <= maxNum : # 제곱수의 multiple배 - 에라토스테네스의 체
        if not square[squareNum * multiple  - minNum] : # 제곱수를 계산하여 제곱수인 경우 answer - 1.
            square[squareNum * multiple  - minNum] = True
            answer -= 1
        multiple += 1

    idx += 1

print(answer)







