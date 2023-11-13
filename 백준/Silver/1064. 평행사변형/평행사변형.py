# 평행사변형. 평행사변형은 평행한 두 변을 가진 사각형이다. 세 개의 서로 다른 점이 주어진다. A(xA,yA), B(xB,yB), C(xC,yC)
# 이때, 적절히 점 D를 찾아서 네 점으로 평행사변형을 만들면 된다. 이때, D가 여러 개 나올 수도 있다.
# 만들어진 모든 사각형 중 가장 큰 둘레 길이와 가장 작은 둘레 길이의 차이를 출력하는 프로그램을 작성하시오. 만약 만들 수 있는 평행사변형이 없다면 -1을 출력한다.
# 첫째 줄에 xA yA xB yB xC yC가 주어진다. 모두 절댓값이 5000보다 작거나 같은 정수이다.
# 첫째 줄에 문제의 정답을 출력한다. 절대/상대 오차는 10-9까지 허용한다.

import sys
input = sys.stdin.readline

xA, yA, xB, yB, xC, yC = map(int, input().rstrip().split())

# 평행사변형 -> 두 쌍의 대변은 길이가 같고, 두 쌍의 대각은 같고, 두 대각선은 서로 다른 대각선을 이등분
# 점 D의 위치를 찾을 필요 없음. 점 3개 -> 3개의 선분 존재. 2개는 같고 하나는 다르기 때문에 길이가 다른 두 선분을 이용하면 된다.
# 세 개의 점이 한개의 선분 위에 있으면 사각형을 못만듬 -> 점 3개의 기울기가 동일 -> 한 개의 기준점을 가지고 다른 두개의 점과 비교하면 된다.

if ((xA - xB) * (yA - yC)) == ((yA - yB) * (xA - xC)) :
    print(-1)
    sys.exit()

abLength = ((xA-xB)**2 + (yA-yB)**2)**0.5
acLength = ((xA-xC)**2 + (yA-yC)**2)**0.5
bcLength = ((xB-xC)**2 + (yB-yC)**2)**0.5

answer = max(abLength, acLength, bcLength) - min(abLength, acLength, bcLength)
print(2*answer)







