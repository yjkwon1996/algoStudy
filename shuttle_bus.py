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

def solution(n, t, m, timetable):
    answer = ''
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
    