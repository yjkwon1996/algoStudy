n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

"""
n명의 권투선수, 1~ n번
경기 결과를 담은 2차원 배열 results
[[A, B], [C, D]] - A가 B를 이기고 C가 D를 이긴다.
정확하게 순위를 매길 수 있는 선수의 수를 return
A에게 진 사람은 A에게 이긴사람에게 이길 수 없다.
A를 이긴 사람은 A에게 진사람에게 무조건 이긴다.
"""
# 각 번호별 사람에게 진사람, 이긴사람 집합
winner, loser = {}, {}
for i in range(1, n+1) :
    winner[i] = set() # winner[i] : i번째 사람이 이긴 사람의 집합
    loser[i] = set() # loser[i] : i번째 사람이 진 사람의 집합

# results를 이용하여 이긴 사람, 진 사람을 집합에 추가
for i in range(1, n+1) :
    for win, lose in results :
        if lose == i : winner[i].add(win)
        if win == i : loser[i].add(lose)
    

    # A에게 진 사람은 A에게 이긴사람에게 이길 수 없다.
    # loser[i] : i에게 진 사람
    # loser[i]는 winner[i]에게 진다.
    for j in loser[i] : winner[j].update(winner[i])
        
    # A를 이긴 사람은 A에게 진사람에게 무조건 이긴다.
    # winner[i] : i에게 이긴 사람
    # winner[i]는 loser[i]를 이긴다.
    for j in winner[i] : loser[j].update(loser[i])
    
# 이긴사람과 진 사람의 합이 n-1이 되면 순위를 정확하게 알 수 있는 선수라는 뜻
answer = 0
for i in range(1, n+1) :
    if len(winner[i]) + len(loser[i]) == n - 1 :
        answer += 1

"""
# 예전에 했던거... 똑같음!

def solution(n, results):
    answer = 0

    win = {}    # win[i] - i에게 진 선수
    lose = {}   # lose[i] - i에게 이긴 선수

    for i in range(1, n+1) : # 중복 제거를 위한 set
        win[i] = set()
        lose[i] = set()

    # results를 순회하면서 win과 lose에 각각의 결과를 추가
    for i in range(1, n+1) :
        for arr in results :
            if arr[0] == i : # i가 이긴 사람을 추가(i에게 진 선수)
                win[i].add(arr[1])
            elif arr[1] == i :
                lose[i].add(arr[0]) # i가 진 사람을 추가(i에게 이긴 선수)

    # lose[i] - i에게 이긴 사람은 i에게 진 사람을 이기고,
    # win[i] - i에게 진 사람은 i에게 이긴 사람을 못이긴다
        for j in lose[i] :
            win[j].update(win[i])
        for j in win[i] :
            lose[j].update(lose[i])

    # win[i] 의 수와 lose[i]의 수가 n-1이라면 정확하게 순위를 매길 수 있는 사람
    for i in range(1, n+1) :
        if len(win[i]) + len(lose[i]) == n - 1 :
            answer += 1

    return answer





"""





