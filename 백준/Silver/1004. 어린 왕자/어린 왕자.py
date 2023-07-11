# 출발점에서 도착점까지 나아가면서 필요한 최소의 행성계 진입/이탈 횟수 구하기
# 출발점이 점 외부/내부에 존재하고, 도착점이 점 내부/외부에 존재하는 경우
# 원의 중심과 출발점/도착점의 거리가 반지름보다 짧으면 내부, 길면 외부에 존재

T = int(input())

for t in range(T) :
    x1, y1, x2, y2 = map(int, input().split()) # 출발점, 도착점
    n = int(input()) # 행성의 개수
    answer = 0
    for _ in range(n) :
        cx, cy, r = map(int, input().split()) # 행성계의 중점, 반지름
        dist1 = (x1 - cx) ** 2 + (y1 - cy) ** 2 # 점과 원의 중심사이의 거리 계산
        dist2 = (x2 - cx) ** 2 + (y2 - cy) ** 2
        if (dist1 < r**2 and dist2 > r**2) or (dist1 > r**2 and dist2 < r**2) : # 행성 경계를 넘는 경우
            answer += 1
            
    print(answer)