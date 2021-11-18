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

# 연결리스트로 해결 가능.
# 연결리스트를 생성해서, 이전 노드와 다음 노드에 대한 정보를 이용한다.
# 이를 이용하여 

def solution(n, k, cmd):
    answer = ''
    
    node = {0 : [n-1, 1]} # key는 행번호. value는 이전 노드번호와 다음 노드번호
    # 첫번째 노드(0행)의 이전 노드는 n-1행
    for i in range(1, n) : 
        if i == n-1 : # 마지막 노드(n-1행)의 다음 노드는 첫번째 노드(0행)
            node[i] = [i-1, 0]
        else : node[i] = [i-1, i+1]
    
    
    remove = [] # 삭제한 행에 대한 기록
    
    for i in cmd :
        if len(i) > 1 : # U나, D일 때
            order, x = i.split(' ')
            cnt = 0
            if order == 'U' : # "U X" : 현재 선택된 행에서 X칸 위에 있는 행을 선택
                while cnt < int(x) : # x값만큼 반복하면서 이전 노드 - node[k][0] - 로 이동
                    k = node[k][0] 
                    cnt += 1
            else : # "D X" : 현재 선택된 행에서 X칸 아래에 있는 행을 선택
                while cnt < int(x) : # x값만큼 반복하면서 다음 노드 - node[k][1] - 로 이동
                    k = node[k][1] 
                    cnt += 1
            
        else :
            if i == 'C' : # "C" : 현재 선택된 행을 삭제 후, 바로 아래 행을 선택. 
                node[node[k][0]][1] = node[k][1]
                node[node[k][1]][0] = node[k][0]
                remove.append([k, node[k]])
                tmp = node[k]
                del node[k]
                
                if tmp[1] == 0 : # 삭제한 행이 마지막 노드라면
                    k = tmp[0] # 선택한 행을 삭제한 노드에서 이전 노드로 선택하게 한다.
                else : k = tmp[1] # 그렇지 않다면 바로 아래 행을 선택
            
            else :# "Z" : 가장 최근에 삭제된 행을 원래대로 복구. 단 현재 선택된 행은 바뀌지 않는다.
                # 삭제 후, 그와 연결된 다른 노드들에 대해서도 정보를 갱신해줘야 한다.
                curr_node, value = remove.pop()
                prev_node, next_node = value
                node[curr_node] = [prev_node, next_node]
                node[prev_node][1] = curr_node
                node[next_node][0] = curr_node 
            
    for i in range(n) :
        if node.get(i) is None :
            answer += 'X'
        else : answer += 'O'
            
    return answer



if __name__ == "__main__" :
    n1, k1, cmd1 = 8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"] # "OOOOXOOO"
    n2, k2, cmd2 = 8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"] # "OOXOXOOO"
    
    print(solution(n1, k1, cmd1))
    print(solution(n2, k2, cmd2))
    
# 일반적인 배열만 단순하게 사용해서 반복문을 돌리는 것보다
# 연결리스트를 통해서 필요한 노드만을 방문하게 하는 것이 훨씬 높은 효율성을 돌릴 수 있다.