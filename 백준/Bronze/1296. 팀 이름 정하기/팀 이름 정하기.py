# 팀 이름 정하기. 연두는 프로그래밍 대회에 나갈 팀 이름을 정하려고 한다. 미신을 믿는 연두는 이환이에게 공식을 하나 받아왔고, 이 공식을 이용해 우승할 확률이 가장 높은 팀 이름을 찾으려고 한다.
#
# 이환이가 만든 공식은 사용하려면 먼저 다음 4가지 변수의 값을 계산해야 한다.
#
# L = 연두의 이름과 팀 이름에서 등장하는 L의 개수
# O = 연두의 이름과 팀 이름에서 등장하는 O의 개수
# V = 연두의 이름과 팀 이름에서 등장하는 V의 개수
# E = 연두의 이름과 팀 이름에서 등장하는 E의 개수
# 그 다음, 위에서 구한 변수를 다음 식에 입력하면 팀 이름의 우승할 확률을 구할 수 있다.
#
# ((L+O) × (L+V) × (L+E) × (O+V) × (O+E) × (V+E)) mod 100
#
# 연두의 영어 이름과 팀 이름 후보 N개가 주어졌을 때, 우승할 확률이 가장 높은 팀 이름을 구해보자. 확률이 가장 높은 팀이 여러가지인 경우 사전 순으로 가장 앞서는 팀 이름이 우승할 확률이 가장 높은 것이다.
#
# 입력
# 첫째 줄에 연두의 영어 이름이 주어진다. 둘째 줄에는 팀 이름 후보의 개수 N이 주어진다. 셋째 줄부터 N개의 줄에 팀 이름이 한 줄에 하나씩 주어진다.
#
# 연두의 영어 이름과 팀 이름은 길이는 1보다 크거나 같고, 20보다 작거나 같으며, 알파벳 대문자로만 이루어져 있다. N은 50보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 우승할 확률이 가장 높은 팀 이름을 출력한다.

import sys
input = sys.stdin.readline

name = input()
N = int(input())
teamName = sorted([input() for _ in range(N)]) # 확률이 동일하면 사전순으로 출력

maxNum = -1
maxIdx = 0

for i in range(N) :
    L = name.count('L') + teamName[i].count('L')
    O = name.count('O') + teamName[i].count('O')
    V = name.count('V') + teamName[i].count('V')
    E = name.count('E') + teamName[i].count('E')

    result = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    if result > maxNum :
        maxNum = result
        maxIdx = i

print(teamName[maxIdx])
