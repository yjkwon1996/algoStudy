N = int(input())
arr = list(map(int, input().split()))
ans = [0]*N

for i in range(N) : # 작은 수부터 채워나가기
    cnt = 0
    for j in range(N) :
        if cnt == arr[i] and ans[j] == 0 : # 큰 사람이 왼쪽에 몇명 있어야 하는지 보고 그만큼 빈자리를 채우기
            ans[j] = i+1
            break
        elif ans[j] == 0 :
            cnt += 1

print(' '.join(map(str, ans)))