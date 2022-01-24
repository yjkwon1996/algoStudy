# 정규 표현식 공부
# regular expression


data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

# 위의 코드를 정규 표현식을 쓴다면?

import re 

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))




# [a-zA-Z] : 알파벳 모두
# [0-9] = [\d] : 숫자
# ^표시 = not 
# \D = 숫자가 아닌 것과 모두 매치







# 점프 투 파이썬
# https://wikidocs.net/4308
