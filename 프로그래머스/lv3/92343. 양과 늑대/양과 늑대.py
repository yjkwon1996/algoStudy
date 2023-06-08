
def solution(info, edges):
    answer = 0
    # 노드를 순회하면서
    # 양의 수가 항상 늑대보다 많아야 함.
    # dfs?
    
    visited = [0 for _ in range(len(info))]
    
    ans = []
    def dfs(sheep, wolf) :
        if sheep > wolf :
            ans.append(sheep)
        else :
            return
        
        for parent, child in edges :
            if visited[parent] and not visited[child] :
                visited[child] = 1
                if info[child] == 0 : # 양이라면
                    dfs(sheep+1, wolf)
                else :  # 늑대라면
                    dfs(sheep, wolf+1)
                visited[child] = 0
    
    # 루트 노드부터 시작. 루트 노드는 항상 0(양)
    visited[0] = 1
    dfs(1, 0)
    
    answer = max(ans)
    
    return answer