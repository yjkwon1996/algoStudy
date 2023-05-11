import sys

N, K = map(int, input().split())

if K < 5 : # a n c t i 5글자는 무조건 배워야함
    print(0)
    exit()
elif K == 26 :  # 알파벳의 모든 글자를 배움
    print(N)
    exit()
    
ans = 0
words = [set(input().rstrip()) for _ in range(N)]
letters = [0] * 26

# 적어도 언어 하나를 배우기 위해서 필수인 a n c t i
for c in ('a', 'n', 'c', 't', 'i') :
    letters[ord(c) - ord('a')] = 1
    
def dfs(idx, cnt) :
    global ans
    
    if cnt == K-5 : # 5글자는 무조건 배웠다는 전제 하에 나머지 배울 문자들을 k-5까지 dfs로 탐색
        wordcnt = 0
        for word in words :
            flag = True
            for w in word :
                if not letters[ord(w) - ord('a')] :
                    flag = False
                    break
            if flag :
                wordcnt += 1
        ans = max(ans, wordcnt)
        return
    
    for i in range(idx, 26) :
        if not letters[i] :
            letters[i] = True
            dfs(i, cnt+1)
            letters[i] = False
            
dfs(0, 0)
print(ans)
    
    