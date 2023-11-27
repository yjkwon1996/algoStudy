# 팩토리얼 0의 개수. N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)
# 첫째 줄에 구한 0의 개수를 출력한다.


import sys
import math
input = sys.stdin.readline

N = int(input().rstrip())

number = str(math.factorial(N))

cnt = 0
for i in range(1, len(number)+1) :
    if number[-i] == '0' :
        cnt += 1
    else :
        break

print(cnt)






