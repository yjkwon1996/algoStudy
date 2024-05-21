import sys
input = sys.stdin.readline

N, Q = map(int, input().rstrip().split())
arr = []
tmp = 0
for _ in range(N) :
    tmp += int(input().rstrip())
    arr.append(tmp)

for _ in range(Q) :
    t = int(input().rstrip())
    
    for i in range(N) :
        if t < arr[i] :
            break
    print(i+1)