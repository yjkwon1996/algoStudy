
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

"""
두개의 단어 begin, target과 단어의 집합 words
한 번에 한개의 알파벳만 바꾸고, words에 있는 단어로만 변환 가능
begin에서 target으로 변환하는 가장 짧은 변환 과정에서 몇 단계를 거치는지 return
한 알파벳만 다른 경우를 찾고, 변환을 반복 수행하다가 target과 동일한 수 발견 시 반복종료
"""

# target이 words에 없으면 0 return
if target not in words :
    print('0')

answer = 0
length = len(begin)
word_arr = [begin] # 변환되는 단어가 담길 배열

# begin과 words가 하나만 다를 경우 begin 변환 가능
while words :
    for word_list in word_arr :
        diff_arr = [] # 변환하기에 한글자만 다른 문자를 담을 배열
        for word in words :
            diff = 0 # 몇 글자 다른지 확인
            for idx in range(length) :
                if word_list[idx] != word[idx] :
                    diff += 1
                if diff > 1 : break # 두글자 이상 다르면 의미x
            if diff == 1 : # 한 글자만 다른 경우
                diff_arr.append(word)
                words.remove(word)
    answer += 1

    # target이 한글자만 다른 배열에 있으면 answer return
    # 그렇지 않으면 현재 단어 배열을 변환한 단어 배열로 치환하고 다시 계산
    if target in diff_arr :
        print(answer)
    else : word_arr = diff_arr

