# 2021 카카오 채용연계형 인턴십
# 표 편집
# https://programmers.co.kr/learn/courses/30/lessons/81303

"""
명령어
"U X" : 현재 선택된 행에서 X칸 위에 있는 행을 선택
"D X" : 현재 선택된 행에서 X칸 아래에 있는 행을 선택
"C" : 현재 선택된 행을 삭제 후, 바로 아래 행을 선택. 삭제된 행이 마지막 행인 경우 바로 윗 행을 선택
"Z" : 가장 최근에 삭제된 행을 원래대로 복구. 단 현재 선택된 행은 바뀌지 않는다.
이 때 최종 표와 처음 표를 비교하여 삭제되지 않은 행은 O, 삭제된 행은 X로 표시하여 문자열 형태로 return
처음 표의 행 개수를 나타내는 정수 n, 처음에 선택된 행의 위치를 나타내는 정수 k
수행한 명령어들이 담긴 배열 cmd 
"""
# 삭제 작업을 수행했을 때, 삭제한 행의 위치를 기억해야 나중에 복구가 가능하다.
# Z를 2번 수행한다면 마지막으로 삭제한 행을 복구한 뒤 마지막 이전에 삭제한 행이 복구된다.
# 현재 선택되어 있는 행의 위치를 기억해야 한다.
# Z 작업 수행 뒤 행이 바뀌지 않는다 = 현재 선택하고 있는 사람을 그대로 계속해서 선택하고 있어야 한다.


# 1차 내맘대로 코드. 실패...
"""
def solution(n, k, cmd):
    answer = ''
    
    remove = [] # 삭제된 행이 몇번째 행인지
    
    size = n
    point = k
    for i in cmd :
        if i[0] == 'U' : # "U X" : 현재 선택된 행에서 X칸 위에 있는 행을 선택
            point -= int(i[2:])
            
        elif i[0] == 'D' : # "D X" : 현재 선택된 행에서 X칸 아래에 있는 행을 선택
            point += int(i[2:])
            
        elif i[0] == 'C' : # "C" : 현재 선택된 행을 삭제 후, 바로 아래 행을 선택. 
            remove.append(point)
            if point == n - 1 : # 삭제된 행이 마지막 행인 경우 바로 윗 행을 선택
                point -= 1
            n -= 1
            
        elif i[0] == 'Z' : # "Z" : 가장 최근에 삭제된 행을 원래대로 복구. 단 현재 선택된 행은 바뀌지 않는다.
            restore = remove.pop()
            if restore <= point - 1 :
                point += 1
            n += 1
            
    for i in range(size) :
        if i in remove :
            answer += 'X'
        else : answer += 'O'
            
    return answer
"""



def solution(n, k, cmd):
    answer = ''
    
    
    return answer





if __name__ == "__main__" :
    n1, k1, cmd1 = 8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"] # "OOOOXOOO"
    n2, k2, cmd2 = 8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"] # "OOXOXOOO"
    
    print(solution(n1, k1, cmd1))
    print(solution(n2, k2, cmd2))