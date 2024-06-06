# 가장 큰 금민수. 은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.
#
# N이 주어졌을 때, N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. N은 4보다 크거나 같고 1,000,000보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 N보다 작거나 같은 금민수 중 가장 큰 것을 출력한다.

import sys
input = sys.stdin.readline

N = int(input())

# 하나씩 빼면서 확인
while True :
    flag = True
    for i in str(N) :
        if i != '4' and i != '7' :
            flag = False
            N -= 1

    if flag :
        print(N)
        break

