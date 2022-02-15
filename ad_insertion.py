# 2021 KAKAO BLIND RECRUITMENT
# 광고 삽입
# https://programmers.co.kr/learn/courses/30/lessons/72414

# 시청자들이 동영상의 어떤 구간을 재생했는지 알 수 있는 재생구간
# 해당 구간을 바탕으로 공익광고가 삽입될 최적의 위치 구하기
# 광고는 원래 영상과 동시에 재생되는 pip형태로 제공
# 동영상 재생 길이 play_time, 공익광고 재생 시간 길이 adv_time
# 시청자들이 해당 동영상을 재생했던 구간 logs
# 시청자들의 누적 재생 시간이 가장 긴 구간에 공익광고를 삽입
# 공익광고의 시작 시간을 구해서 return. 누적 재생시간이 가장 많은곳이 여러곳이라면 가장 빠른 시간을 return
# 


# 광고의 재생시간 길이와 동영상 재생 길이, 시청자들의 재생구간을 비교하여
# 가장 많은 시청자가 광고를 볼 수 있도록
# 시간을 초단위로 변환하여 계산하기 편하게 하고
# 시청자 수를 기록하여 누적된 시청자 수를 바탕으로 가장 시청자수가 많은 구간 탐색
# 간만이라...

# 시간을 초 단위로 변환
def sec_conv(time) :
    hour, minute, second = time.split(':') # :를 기준으로 시, 분 초 단위를 나눈뒤 초 단위로 환산하여 return
    return int(hour) * 3600 + int(minute) * 60 + int(second)    


def solution(play_time, adv_time, logs):
    answer = ''
    
    # 시간을 초 단위로 변환
    play_time = sec_conv(play_time)
    adv_time = sec_conv(adv_time)
    all_time = [0 for i in range(play_time + 1)] # all_time[i] = i 시간에 시청중인 시청자 수
    
    # 로그 내 시간을 초 단위로 변환, 시청 시작시간과 끝 시간을 표시
    for i in logs : # 로그의 시작시간과 끝시간을 나눠서 초단위로, 구간별 시청자수 기록에 추가
        start, end = i.split('-')
        start = sec_conv(start)
        end = sec_conv(end)
        all_time[start] += 1
        all_time[end] -= 1 # 시청을 종료한 시간에도 -1을 해줘야 사람 수가 맞게 떨어짐
        
    # 구간별 시청자 수 기록
    for i in range(1, len(all_time)) :
        all_time[i] = all_time[i] + all_time[i-1]
        
    # 모든 시청자수 누적 기록
    for i in range(1, len(all_time)) :
        all_time[i] = all_time[i] + all_time[i-1]
    
    
    # 누적된 시청자수 기록을 통해서 가장 시청자수가 많은 구간 찾기
    # 처음부터 끝까지 탐색하면서 구간대비 시청자수가 가장 많은 곳
    # 현재 i의 누적 시청자수에서 i-adv_time의 누적 시청자수를 빼면 해당 구간의 시청자수 값.
    max_view = 0
    max_time = 0
    for i in range(adv_time - 1, play_time) :
        if i >= adv_time : 
            if max_view < all_time[i] - all_time[i-adv_time] :
                max_view = all_time[i] - all_time[i-adv_time]
                max_time = i - adv_time + 1
        else :
            if max_view < all_time[i] :
                max_view = all_time[i]
                max_time = i - adv_time + 1
    
                
    h = max_time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    max_time = max_time % 3600
    m = max_time // 60
    m = '0' + str(m) if m < 10 else str(m)
    max_time = max_time % 60
    s = '0' + str(max_time) if max_time < 10 else str(max_time)
    answer = h + ':' + m + ':' + s
    
    return answer




"""
다른사람꺼

def solution(play, adv, logs):
    c = lambda t: int(t[0:2]) * 3600 + int(t[3:5]) * 60 + int(t[6:8])
    play, adv = c(play), c(adv)
    logs = sorted([s for t in logs for s in [(c(t[:8]), 1), (c(t[9:]), 0)]])

    v, p, b = 0, 0, [0] * play
    for t, m in logs:
        if v > 0:
            b[p:t] = [v] * (t - p)
        v, p = v + (1 if m else -1), t

    mv, mi = (s := sum(b[:adv]), 0)
    for i, j in zip(range(play - adv), range(adv, play)): # 구간합을 구할 때, 투포인터 사용
        s += b[j] - b[i]
        if s > mv:
            mv, mi = s, i + 1

    return f"{mi//3600:02d}:{mi%3600//60:02d}:{mi%60:02d}"


"""
























if __name__ == "__main__" :
    play_time1 = "02:03:55"
    adv_time1 = "00:14:15"
    logs1 = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
    # reseult = "01:30:59"
    
    play_time2 = "99:59:59"
    adv_time2 = "25:00:00"  
    logs2 = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
    # result = "01:00:00"
    
    play_time3 = "50:00:00"
    adv_time3 = "50:00:00"
    logs3 = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
    # result = "00:00:00"
    
    print(solution(play_time1, adv_time1, logs1))
    print(solution(play_time2, adv_time2, logs2))
    print(solution(play_time3, adv_time3, logs3))
    
    