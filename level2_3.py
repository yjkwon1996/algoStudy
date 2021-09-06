s = "110010101001"	
"""
0과 1로 이루어진 문자열 x에 대한 이진 변환
x의 길이를 c, x를 c를 2진법으로 표현한 문자열
0과 1로 이루어진 문자열 s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가한다
이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 배열에 담아 return
format(32, b)
"""

answer = []
char = '0'
cnt = 0
num = 0
while True :
    for x in range(len(char)) : # 문자열에서 0을 제거하고 제거한 수를 cnt에 +
        cnt += s.count('0')
        string = s.replace(char[x],'')
        # 0을 제거한 2진수 string, 길이는 len(string)
        # len(string)을 다시 이진 변환
        s = str(format(len(string), 'b'))
        num += 1
    if s == '1' : 
        answer.append(num)
        answer.append(cnt)
        break
    
