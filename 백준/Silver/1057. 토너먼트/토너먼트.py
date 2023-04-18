N, start, end = map(int, input().split()) # N명 출전, 1라운드에서의 김지민 번호와 임한수 번호
cnt = 0; # 몇번째 라운드에서 만날지
while start != end : # 매 라운드마다 // 2 번호를 배정받음. 둘의 번호가 같으면 만나는 라운드
    start -= start // 2
    end -= end // 2
    cnt += 1
print(cnt)
    