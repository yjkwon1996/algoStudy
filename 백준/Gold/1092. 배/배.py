import sys

N = int(input())
crane = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
box = sorted(list(map(int, input().split())), reverse=True)

if (max(box) > max(crane)) : # 크레인으로 못옮기는 물건이 있으면
    print(-1)
    sys.exit()

ans = 0 
while box :
    if not box : # 모든 박스를 옮겼다면
        break

    for c in crane : # 크레인으로
        for b in box : # 모든 박스를 보면서
            if c >= b : # 옮길 수 있는 박스를 찾아서
                box.remove(b) # 옮기기
                break
    ans += 1

print(ans)
