def solution(n, weak, dist):
    answer = 0 
    print(n, weak, dist)
    # 외벽의 길이 n, 취약 지점의 위치가 담긴 배열 weak, 각 친구가 1시간동안 이동할 수 있는 거리가 담긴 배열 dist
    # 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최소값을 리턴
    # 이동 거리가 큰 친구순으로 정렬하면 제일 처음 찾는 경우가 친구수의 최소값일듯?
    
    repairs = [()] # 고칠 수 있는 취약점
    
    dist.sort(reverse=True) # 이동할 수 있는 거리가 큰 순서대로 정렬해서
    
    # 모든 취약 지점이 수리되었는지 확인
    for move in dist :
        repair = [] # 친구 별 고칠 수 있는 취약점들 저장
        answer += 1
        
        # 수리 가능한 지점
        for idx, start in enumerate(weak) :
            end = weak[idx:] + [n+i for i in weak[:idx]] # 시작점 기준 끝점
            point = [e % n for e in end if e - start <= move] # 가능한 지점 저장
            repair.append(set(point)) # 집합으로 수리가 가능한 지점들을 담기

        # 수리가 가능한 경우
        repair_lst = set()
        for r in repair : # 새로운 친구의 수리 가능 지점
            for i in repairs : # 기존의 수리 가능지점
                new = r | set(i) # 새로운 수리 가능지점
                if len(new) == len(weak) : # 모두 수리시, 친구 수 리턴
                    return answer
                repair_lst.add(tuple(new))
        repairs = repair_lst
        
    return -1 # 취약 점검을 전부 점검하지 못하면 -1