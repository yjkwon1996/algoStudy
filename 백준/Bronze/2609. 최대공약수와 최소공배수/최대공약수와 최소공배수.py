# 최대공약수와 최소공배수. 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
# 유클리드 호제법

import sys
import math
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())

print(math.gcd(A, B))
print(math.lcm(A, B))






