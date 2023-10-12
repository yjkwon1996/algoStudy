# 약수. 양수 A가 N의 진짜 약수가 되려면 N이 A의 배수이고 A가 1과 N이 아니어야함
# 어떤 수 N의 진짜 약수가 주어질 때 N을 구하기

import sys
input = sys.stdin.readline

num = int(input().rstrip()) # N의 진짜 약수의 개수
div = list(map(int, input().rstrip().split())) # N의 진짜 약수

# 가장 작은 약수와 가장 큰 약수를 곱하면 N이 나옴
div.sort()

print(div[0] * div[-1])

