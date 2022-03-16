# 2447 별 찍기
# https://www.acmicpc.net/problem/2447

# 재귀적인 패턴으로 별을 찍기
# N이 3의 거듭제곱(3, 9, 27...)이라고 할 때 크기 N의 패턴은 N X N 정사각형 모양
# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴
# ***
# * *
# ***
# N이 3보다 큰 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)X(N/3) 정사각형을 크기 (N/3)의 패턴으로 둘러싼 형태

# N = 3^1 일 때는 가운데를 비워두고 별이 찍히고,
# N = 3^i 일 때는 가운데를 비워두고 N = 3^(i-1) 일 때의 별이 각각의 위치에 찍힌다.
# 일부분이 전체와 같은 구조(프렉탈 구조)

def star_point(N) :
    arr = []
    for i in range(3 * len(N)) :
        if i // len(N) == 1 : # 가운데를 비워두기 위한 조건문
            arr.append(N[i % len(N)] + " " * len(N) + N[i % len(N)])
        else :
            arr.append(N[i % len(N)] * 3)
    return arr

N = int(input())
star_arr = ['***', '* *', '***']
e = 0 # 지수 확인

while N != 3 : # 지수 계산. 입력받은 N의 지수 - 1 
    N = int(N / 3)
    e += 1
    
for i in range(e) : # N = 27이라면 N = 9 일때의 패턴을 star_arr에 저장하고 반복해서 출력한다.
    star_arr = star_point(star_arr)
for i in star_arr :
    print(i)


