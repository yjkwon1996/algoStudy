# 10814 나이순 정렬
# https://www.acmicpc.net/problem/10814

"""
사람들의 나이와 이름이 공백으로 구분되어 주어짐. 
회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 기입한 사람이 앞에 오는 순서대로 정렬하는 프로그램
"""
# 첫째 줄에 회원 수 N(1이상 10000이하)
# 둘째 줄부터 N개의 줄에 각 회원의 나이와 이름이 공백으로 구분되서 주어진다.
# 나이는 1이상 200이하인 정수
# 이름은 알파벳 대소문자, 길이가 100이하인 문자열

N = int(input())

info = []
for i in range(N) :
    age, name = map(str, input().split())
    info.append((int(age), name)) # 입력하면서 기입 순서대로 정렬이 되게끔
    
info.sort(key=lambda x : x[0]) # 이미 입력 순서대로 정렬되어 있으므로 나이 순으로 정렬

for i in range(N) :
    print(info[i][0], info[i][1])
