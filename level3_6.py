def solution(a, b, g, s, w, t):
    """
    금 a, 은 b : 필요한 광물의 양
    i번 도시에는 금 g[i], 은 s[i]가 있다. 각 도시는 하나의 트럭을 보유중
    한번 운송 : 편도 이동에 t[i]시간이 걸리고 w[i] 광물을 운반 가능
    새로운 도시를 건설하기 위해 금 a와 은 b를 전달할 수 있는 가장 빠른 시간을 return
    """
    # 어렵다...
    # 이분탐색을 이용한 결정 문제. 운반에 걸리는 최소시간을 찾기
    # 제한 시간 내에 금 우선으로 운반했을 때 금과 은의 양 : g_max, s_min
    # 제한 시간 내에 은 우선으로 운반했을 때 금과 은의 양 : g_min, s_max
    # g_max + s_min = g_min + s_max
    # a <= g_max, b <= s_max, a+b <= g_max+s_min= g_min_s_max 조건을 만족한다면
    # 제한 시간 내에 금 a와 은 b 운반이 가능
    
    # 운반에 걸리는 최악의 시간 : 왕복(2) * 금, 은2종(2) * 광물의 최대무게(10**9) * 도시의 최대갯수(10**5)
    end = 4 * (10**9) * (10**5)
    start = 0
    answer = 4 * (10**9) * (10**5)
    # 이분 탐색
    while start <= end :
        mid = (start+end) // 2
        gold = 0
        silver= 0
        total = 0
        
        for i in range(len(g)) : # 도시 수만큼 반복하며
            # 주어진 시간 내에서 이동할 수 있는 횟수(왕복)
            move_cnt = mid // (t[i] * 2)
            if mid % (t[i] * 2) >= t[i] : # 편도 추가
                move_cnt += 1
            
            gold += g[i] if (g[i] < move_cnt * w[i]) else move_cnt * w[i]
            silver += s[i] if (s[i] < move_cnt * w[i]) else move_cnt * w[i]
            total += g[i] + s[i] if (g[i]+s[i] < move_cnt * w[i]) else move_cnt * w[i]
            
        if gold >= a and silver >= b and total >= a+b :
            end = mid - 1
            answer = min(answer, mid)
        else :
            start = mid + 1

    return answer




if __name__ == "__main__" :
    # a, b = 10, 10
    # g, s, w, t = [100], [100], [7], [10]
    # result = 50
    
    a, b = 90, 500
    g, s, w, t = [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]
    # result = 499
    print(solution(a, b, g, s, w, t))