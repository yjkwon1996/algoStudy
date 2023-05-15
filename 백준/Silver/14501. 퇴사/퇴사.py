N = int(input())
TP = [list(map(int, input().split())) for _ in range(N)]
    
arr = [0 for _ in range(N+1)]

for i in range(N) :
    for j in range(i+TP[i][0], N+1) : # 상담이 가능한 날짜
        if arr[j] < arr[i] + TP[i][1] : # 기존에 계산했던 최대 수익보다 더 크면 갱신
            arr[j] = arr[i] + TP[i][1]

print(arr[N]) # 마지막 값을 출력하면 된다.
        