N, M = map(int, input().split())
arrA = []
arrB = []
for _ in range(N) :
    arrA.append(list(map(int, list(input()))))
for _ in range(N) :
    arrB.append(list(map(int, list(input()))))
    

def reverse(x, y) : # 뒤집기
    for i in range(x, x+3) :
        for j in range(y, y+3) :
            if arrA[i][j] == 0 :
                arrA[i][j] = 1
            else :
                arrA[i][j] = 0

cnt = 0
if (N<3 or M<3) and arrA != arrB :
    cnt -= 1
else :
    for i in range(N-2) :
        for j in range(M-2) :
            if arrA[i][j] != arrB[i][j] :
                cnt += 1
                reverse(i, j)
    
if cnt != -1 :
    if arrA != arrB :
        cnt = -1
print(cnt)