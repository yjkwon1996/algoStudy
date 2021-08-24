

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

"""
선수의 수 n, 경기 결과를 담은 2차원 배열 results
정확하게 순위를 매길 수 있는 선수의 수를 return
[A, B] -> A가 B를 이긴다.
[B, C], [B, D] -> B가 C, D를 이긴다
-> A는 B, C, D를 이긴다
"""
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
