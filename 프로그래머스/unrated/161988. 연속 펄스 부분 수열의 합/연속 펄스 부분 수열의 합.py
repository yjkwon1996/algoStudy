def solution(sequence):
    answer = 0
    
    # 펄스 수열은 - + - + ...
    # -로 시작하는 펄스와 +로 시작하는 펄스를 나눠서 생각
    # -1 ** 1 , -1 ** 2, -1 ** 3 ...으로 구현
    dp1 = [sequence[i] * (-1) ** i for i in range(len(sequence))] 
    dp2 = [sequence[i] * (-1) ** (i+1) for i in range(len(sequence))]
    # 변화하지 않는 연속 펄스를 적용한 sequence가 필요함
    seq1 = [sequence[i] * (-1) ** i for i in range(len(sequence))] 
    seq2 = [sequence[i] * (-1) ** (i+1) for i in range(len(sequence))] 
    
    for i in range(len(sequence)) :
        if i >= 1 :
            dp1[i] = max(dp1[i-1]+seq1[i], seq1[i])
            dp2[i] = max(dp2[i-1]+seq2[i], seq2[i])

    answer = max(max(dp1), max(dp2))
    return answer