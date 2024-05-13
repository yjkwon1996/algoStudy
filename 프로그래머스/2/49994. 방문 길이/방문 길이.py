def solution(dirs):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]
    direction = ["U", "D", "R", "L"]

    x, y = 0, 0
    visited = set()

    visited.add((x, y))
    for dir in dirs :
        d = direction.index(dir)
        nx = x + dx[d]
        ny = y + dy[d]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add(((x, y), (nx, ny))) # 출발점과 도착점 구분이 없음 - 루프 돌 때 문제가 발생
            visited.add(((nx, ny), (x, y))) # 둘 다 추가하고 마지막에 2로 나누면
            x = nx
            y = ny

    answer = len(visited) // 2
    return answer