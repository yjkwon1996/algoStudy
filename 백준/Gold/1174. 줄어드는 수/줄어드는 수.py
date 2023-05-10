N = int(input())
ans = set() # 중복 수 체크용 집합
num = []
def dfs() :
    global ans
    global num
    if num : # 모든 수를 다 확인했다면 결과값을 추가
        ans.add(int("".join(map(str, num))))
    for i in range(10) : # 0부터 9까지 줄어드는 수
        if not num or num[-1] > i : # 마지막 값이 더 큰 경우
            num.append(i)
            dfs()
            num.pop()
    
dfs()

ans = list(ans) # 배열로 만들어서 
ans.sort()

if len(ans) >= N :
    print(ans[N-1])
else : print(-1)