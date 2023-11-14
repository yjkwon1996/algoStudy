# 책 페이지. 지민이는 전체 페이지의 수가 N인 책이 하나 있다. 첫 페이지는 1 페이지이고, 마지막 페이지는 N 페이지이다. 각 숫자가 전체 페이지 번호에서 모두 몇 번 나오는지 구해보자.
# 첫째 줄에 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.
# 첫째 줄에 0이 총 몇 번 나오는지, 1이 총 몇 번 나오는지, ..., 9가 총 몇 번 나오는지를 공백으로 구분해 출력한다.

import sys
input = sys.stdin.readline

N = int(input().rstrip())

# 1의자리는 항상 변화함 0 ~ 9. 10의 자리는 10마다 변화하고, 100은 100마다 변화
# 크게 하여 계산 후, 차이만큼 다시 계산하면?
# ex) 55 -> 59 - 1 ~ 5는 10의 자릿수와 1의 자릿수 모두 존재
# 이후 일의 자리 9-5인 4만큼만 해주듯이

answer = [0 for _ in range(10)] # 각 자릿수

unit = 1 # 10의 자리, 1의자리 등 단위
for i in range(len(str(N))) :
    tmp = int(str(N//10) + "9")
    value = tmp - N

    # for j in range(10-value) :
    #     answer[j] += (N // 10 + 1) * unit

    # 미리 추가한 만큼의 값만큼 더해주고, 차이만큼 빼기
    # 자리수도 고려하여 해야함
    for j in range(10) :
        answer[j] += (N // 10 + 1) * unit
    for j in range(10-value, 10) :
        answer[j] -= unit

    for num in list(str(N)[:-1]) :
        answer[int(num)] -= value * unit

    answer[0] -= unit

    N = N // 10
    unit *= 10

print(*answer)




