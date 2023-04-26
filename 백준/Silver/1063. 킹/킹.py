king, stone, N = input().split() # 킹의 위치, 돌의 위치, 움직이는 횟수
N = int(N)

king = [ord(king[0]) - ord("A") + 1, int(king[1])]
stone = [ord(stone[0]) - ord("A") + 1, int(stone[1])]

move = ["R", "L", "B", "T", "RT", "LT", "RB", "LB"] # 각 위치에 맞게
dx = [1, -1, 0, 0, 1, -1, 1, -1] 
dy = [0, 0, -1, 1, 1, 1, -1, -1]

while N>0 :
    order = input()
    d = move.index(order)
    
    dking = [king[0] + dx[d], king[1] + dy[d]]
    dstone = [stone[0] + dx[d], stone[1] + dy[d]]
    
    if 1<=dking[0]<= 8 and 1<=dking[1]<=8 : # 범위 안에서
        if dking == stone : # 같은 위치라면
            if 1<=dstone[0]<=8 and 1<=dstone[1]<=8 :  # 범위 안에서 한칸 밀기
                king = dking
                stone = dstone
        else : # 다른 위치면
            king = dking # 킹만 이동
    N -= 1
    
print(chr(king[0] + ord("A") -1) + str(king[1]))
print(chr(stone[0] + ord("A") -1) + str(stone[1]))

