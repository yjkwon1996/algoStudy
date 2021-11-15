# 2018 KAKAO BLIND RECRUITMENT
# [1차] 셔틀버스
# https://programmers.co.kr/learn/courses/30/lessons/17678


"""
셔틀은 09:00부터 총 n회 t분 간격으로 역에 도착하며 하나의 셔틀에는 최대 m명의 승객이 탑승가능
셔틀은 도착한 순간에 대기열에 선 사람부터 대기 순서대로 태운다. 09:00에 도착한 셔틀은 09:00에 줄선 사람도 탑승가능
콘이 셔틀을 타고 사무실로 갈 수 있는 도착시간 중 가장 늦은 시간을 구하라.
콘은 같은 시간에 도착한 사람 중 제일 뒤에 대기. 모든 사람은 23:59에 집에 돌아간다.
timetable은 하루 동안 사람이 대기열에 도착하는 시간이 hh:mm으로 적혀있음.
"""
# 셔틀은 09:00 부터 t분 간격으로 n회 출발함. 하나의 셔틀에는 최대 m명이 탑승 가능하다.
# 콘은 timetable에서 같은 시간대에 도착한 사람 중 가장 마지막으로 탑승한다.
# n과 cnt, timetable과 m을 생각.
# 모든 시간을 분단위로 환산해서 계산한다. 09:00 -> 9*60 = 540
# 버스에 탈 수 있는 인원과 timetable을 비교해서
# 버스에 자리가 남는 경우 ->  콘은 버스 도착 시간에 도착하면 된다.
# 버스에 자리가 없을 경우 -> 마지막에 탄 사람보다 1분 먼저 도착하면 된다.

def solution(n, t, m, timetable):
    answer = ''
    # timetable의 시간을 분단위로 환산. 본래 데이터는 문자열이기 때문에 정수형으로
    min_timetable = [int(time[:2]) * 60 + int(time[3:5]) for time in timetable]
    min_timetable.sort()
    
    last_bus = 60 * 9 + (n - 1) * t # 09:00 부터 t분 간격으로 n회 출발했을 때 마지막 배차시간
    
    for i in range(n) : # 배차 횟수(n)만큼 반복
        if len(min_timetable) < m : # timetable의 모든 사람을 한번에 태울 수 있다면
        # 이 구간에서 min_timetable대신 timetable 사용 시 런타임 에러 발생. 왜?
        # len(timetable)과 len(min_timetable)이 다르다?
            return '%02d:%02d' % (last_bus // 60, last_bus % 60) # 마지막 배차시간때 와서 탑승하면 된다.
        if i == n - 1 : # 마지막 배차시간이라면
            if min_timetable[0] <= last_bus : # 마지막 배차 보다 일찍 온 사람이 있으면(버스에 자리가 없으면)
                last_bus = min_timetable[m - 1] - 1 # 마지막에 탄 사람보다 1분 먼저 도착하면 된다.
            return '%02d:%02d' % (last_bus // 60, last_bus % 60)
        for j in range(m-1, -1, -1) : # 거꾸로 반복문을 돌려서 인덱스 관련 문제 해
            next_bus = (60 * 9) + i * t # 다음 배치시간을 분단위로 계산
            if min_timetable[j] <= next_bus : # 다음 배차때 탑승할 사람을 timetable에서 삭제
                del min_timetable[j]

    return answer




if __name__ == "__main__" :
    n1, t1, m1, timetable1 = 1, 1, 5, ["08:00", "08:01", "08:02", "08:03"] # "09:00"
    n2, t2, m2, timetable2 = 2, 10, 2, ["09:10", "09:09", "08:00"] # "09:09
    n3, t3, m3, timetable3 = 2, 1, 2, ["09:00", "09:00", "09:00", "09:00"] # "08:59"
    n4, t4, m4, timetable4 = 1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"] # "00:00"
    n5, t5, m5, timetable5 = 1, 1, 1, ["23:59"] # "09:00"
    n6, t6, m6, timetable6 = 10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"] # "18:00"
    print(solution(n1, t1, m1, timetable1))
    print(solution(n2, t2, m2, timetable2))
    print(solution(n3, t3, m3, timetable3))
    print(solution(n4, t4, m4, timetable4))
    print(solution(n5, t5, m5, timetable5))
    print(solution(n6, t6, m6, timetable6))
    
    n, t, m, timetable = 10, 60, 10,  ["17:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
    print(solution(n, t, m, timetable))
    # 마지막 배차 시간에 있어서 오류가 발생?
