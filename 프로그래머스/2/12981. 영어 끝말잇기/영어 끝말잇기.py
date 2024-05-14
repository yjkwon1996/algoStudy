def solution(n, words):
    answer = [0, 0]
    arr = []
    arr.append(words[0])
    person = 2
    cnt = 1
    for i, word in enumerate(words[1:], start=1) :
        if words[i-1][-1] != word[0] : # 끝말잇기가 틀린 경우
            answer = [person, cnt]
            break
        elif word in arr : # 이미 했던 말을 또 하는 경우
            answer = [person, cnt]
            break
        arr.append(word)
        person += 1
        if person > n :
            person = 1
            cnt += 1

    return answer