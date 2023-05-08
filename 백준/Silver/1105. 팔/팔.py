L, R = map(str, input().split(' ')) # 문자열 형식으로 처리

cnt = 0
if len(L) != len(R) : # 자릿수가 다르면 8이 하나도 없는 수가 무조건 존재함
    print(0)
else :
    for i in range(len(L)) : # 가장 큰 자릿수부터 그 다음 자릿수로 내려가면서 
        if L[i] == R[i] : # L과 R 둘 다 8이면 카운트하고, 둘 중 하나라도 8이 아니라면 끝
            if L[i] == '8' : # 두 숫자의 일부가 동일해야함
                cnt += 1
        else :
            break
    print(cnt)
                
    