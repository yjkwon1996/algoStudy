from collections import deque

N, K = map(int, input().split()) # 벨트 길이, 내구도가 0인 칸의 개수가 K개 이상이면 반복 종료
A = deque(list(map(int, input().split()))) # 내구도
robot = deque([0]*N)

ans = 0
while True :
    ans += 1 # 몇번째 반복인지
    A.rotate(1) # 벨트 회전
    robot.rotate(1) # 로봇도 회전

    robot[-1] = 0 # 로봇이 내리는 위치에 있으면 제거
    
    for i in range(N-2, -1, -1) : # 로봇 이동
        if A[i+1] >= 1 and robot[i+1] == 0 and robot[i] == 1 : # 내구도가 1 이상 남았으며, 이동하려는 칸에 로봇이 없으면 이동
            robot[i] = 0
            robot[i+1] = 1
            A[i+1] -= 1 # 내구도 1 감소
    robot[-1] = 0 # 이동 후 내리는 위치에 있으면 제거

    if A[0] != 0 and robot[0] != 1 : # 로봇 올리기
        robot[0] = 1
        A[0] -= 1
    
    if A.count(0) >= K : # 내구도 0인 칸이 K개 이상이면 끝
        break
print(ans)


