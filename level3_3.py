routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]

"""
고속도로 카메라를 한번은 만나도록
경로 routes. 최소 몇대의 카메라를 설치해야 하는지 return
routes[[a, b], [c, d]] - 첫번째 차량 경로 a, b. 두번째 차량 경로 c, d
a, c 진입. b, d 진출
"""
# 진출 기점 정렬 후 카메라와 만나는지 확인
routes.sort(key=lambda x : x[1])
idx = -30001 # 차량의 진입, 진출 지점은 -30000 이상 30000 이하. -30000부터 탐색 시작
answer = 0

for i in routes :
    if idx < i[0] :
        answer += 1
        idx = i[1]

"""
# 예전에 했던거. 똑같음!

def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1])
    camera_loc = -30001
    for i in routes :
        if camera_loc < i[0] :
            answer += 1
            camera_loc = i[1]


    return answer

"""