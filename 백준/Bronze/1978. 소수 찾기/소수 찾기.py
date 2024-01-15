# 소수 찾기. 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
#
# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

import sys
input = sys.stdin.readline

N = int(input().rstrip())
number = list(map(int, input().rstrip().split()))

cnt = 0
for num in number :
    flag = True # 소수 체크용
    if num > 1 :
        for i in range(2, num) :
            if num % i == 0 : # 2부터 num까지의 수 중에서 나누어 떨어지면 소수가 아님
                flag = False
                break
        if flag :
            cnt += 1

print(cnt)



