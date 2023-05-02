N = int(input())
name = []

for i in range (N) :
    order = input()
    name.append(order)
    
ans = list(name[0])

for i in range(N) :
    for j in range(len(ans)) :
        if name[i][j] == ans[j] :
            continue
        else :
            ans[j] = '?' # 글자가 다르면 ?

print(''.join(ans))
