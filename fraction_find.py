# 1193 분수찾기
# https://www.acmicpc.net/problem/1193

# 무한히 큰 배열에 분수가 있을 때, 지그재그 순서대로 차례로 진행한다면
# x가 주어졌을 때 x번째 분수를 구하는 프로그램

# 1/1 시작* - 분모 1증가(1/2) - 분모1감소, 분자1증가(2/1)* - 분자1증가(3/1) - 분자1감소, 분모1증가(2/2)
# 분자1감소, 분모1증가(1/3)* - 분모1증가(1/4)
# *이후 분모만 1증가 or 분자만 1증가를 번갈아 가고
# 분모 증가시, 이후 진행은 카운터동안 분모감소,분자증가.
# 분자 증가시, 이후 진행은 카운터동안 분자감소, 분모증가
# 매 *마다 진행하는 카운터도 1씩 증가

# 분자 = 1, 12, 321, 1234, 54321 ...
# 분모 = 1, 21, 123, 4321, 12345 ...

# ex) x = 5

x = int(input())

counter = 1
while x > counter : # 변수로 주어진 x의 위치를 배열에서 찾기 위해
    x -= counter    # 변수 x가 대각선 counter 수보다 작아질 때 해당하는 대각선에 변수 x가 있다는 것
    counter += 1    # x = 2, counter = 3. 즉 3번째 지그재그때 x의 위치가 존재
    
# 몇번째 지그재그인지 파악했다면 
if counter % 2 == 0 :               # counter가 짝수라면
    numerator = x                   # 분자
    denominator = counter - x + 1   # 분모
else :                              # counter가 홀수라면
    numerator = counter - x + 1
    denominator = x

print(str(numerator) + '/' + str(denominator))


