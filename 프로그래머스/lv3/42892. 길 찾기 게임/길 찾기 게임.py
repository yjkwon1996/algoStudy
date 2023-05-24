import sys
sys.setrecursionlimit(10**6)

# 트리를 위한 클래스
class Tree :
    def __init__(self, data, left, right) :
        self.data = data # idx
        self.left = left
        self.right = right

# 재귀 방식으로 트리 구성하기
def makeTree(nodeinfo, dictionary) :
    if len(nodeinfo) == 0 : # 더이상 추가할 자식 노드가 없다면 되돌아가기
        return None
    
    nodeinfo.sort(key=lambda x: x[1], reverse=True) # y축 기준 높은순서부터 정렬
    root = tuple(nodeinfo[0]) # 각각의 시작점 노드 좌표
    nodenumber = dictionary[root] # 노드 idx
    nodeinfo.pop(0) # root 노드를 빼고 그 아래의 노드들을 left, right로 나눈다
    
    rootx = root[0] # root노드의 x좌표를 기준으로 좌우로 나누기
    leftnode = []
    rightnode = []
    for x in nodeinfo :
        if x[0] < rootx :
            leftnode.append(x)
        else :
            rightnode.append(x)

    del dictionary[root] # 현재 노드를 제거하고 왼쪽, 오른쪽으로 나눠서 다시 트리 구조 만들기
    return Tree(nodenumber, makeTree(leftnode, dictionary), makeTree(rightnode, dictionary))

# 전위 순회
def preOrder(tree, lst) :
    if tree == None :
        return
    lst.append(tree.data)
    preOrder(tree.left, lst)
    preOrder(tree.right, lst)
    return lst

# 후위 순회
def postOrder(tree, lst) :
    if tree == None :
        return
    postOrder(tree.left, lst)
    postOrder(tree.right, lst)
    lst.append(tree.data)
    return lst

def solution(nodeinfo):
    answer = [[], []]
    dictionary = dict()
    for i, x in enumerate(nodeinfo) : # 인덱스를 붙여주기
        dictionary[tuple(x)] = i+1
        
    # 트리 만들기
    tree = makeTree(nodeinfo, dictionary)
    
    # 전위순회 후위순회
    pre = preOrder(tree, [])
    post = postOrder(tree, [])
    answer[0] = pre
    answer[1] = post
    
    return answer