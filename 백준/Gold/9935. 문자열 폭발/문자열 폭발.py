# 문자열 폭발. 문자열에 폭발 문자열을 심어 놓았다. 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 된다.

# 문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다. 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.
# 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
# 폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.
# 상근이는 모든 폭발이 끝난 후에 어떤 문자열이 남는지 구해보려고 한다. 남아있는 문자가 없는 경우가 있다. 이때는 "FRULA"를 출력한다.
# 폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.

# # 시간초과
#
# import sys
# input = sys.stdin.readline
#
# s = list(input().rstrip())
# bomb = list(input().rstrip())
#
# length = len(bomb)
# idx = 0
# while idx <= len(s) - length :
#     if s[idx:idx+length] == bomb :
#         del s[idx:idx+length]
#         idx -= length
#
#     idx += 1
#
# if s :
#     print(''.join(s))
# else :
#     print('FRULA')

# 스택에 하나씩 넣으면서?
import sys
input = sys.stdin.readline

s = input().rstrip()
bomb = input().rstrip()

length = len(bomb)
stack = []

for i in range(len(s)) :
    stack.append(s[i])
    if ''.join(stack[-length:]) == bomb : # 추가한걸 뒤에서부터 확인하면서 같은 문자를 쌓았다면 제거
        for _ in range(length) :
            stack.pop()


if stack :
    print(''.join(stack))
else :
    print('FRULA')


