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


def solution(play_time, adv_time, logs):
    answer = ''
    
    
    
    


    
    return answer


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
    
    