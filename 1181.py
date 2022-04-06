# 1181 단어 정렬
# https://www.acmicpc.net/problem/1181

"""
알파벳 소문자로 이루어진 N개의 단어가 들어오면
1. 길이가 짧은 순으로
2. 길이가 같으면 사전 순으로
정렬하는 프로그램을 작성하시오.
"""
# 첫째 줄에 단어의 개수 N(1 <= N <= 20000)이 주어지고
# 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다.
# 주어진 문자열의 길이는 50을 넘지 않음
# 같은 단어가 여러 번 입력된 경우, 한번만 출력 - set

N = int(input())

txt_arr = []

for i in range(N) :
    txt_arr.append(input())
    
txt_arr = list(set(txt_arr)) # 중복 제거
txt_arr.sort(key=lambda x : (len(x), x)) # 길이순, 사전순 정렬

print("\n".join(txt_arr)) # join : 리스트를 문자열로. \n을 이용하여 각 배열을 줄마다 출력할 수 있음


