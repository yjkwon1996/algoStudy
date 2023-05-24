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
    if len(nodeinfo) == 0 :
        return None
    
    nodeinfo.sort(key=lambda x: x[1], reverse=True) # y축 기준 높은순서부터 정렬
    root = tuple(nodeinfo[0])
    nodenumber = dictionary[root]
    nodeinfo.pop(0)
    
    rootx = root[0] # root노드의 x좌표를 기준으로 좌우로 나누기
    leftnode = []
    rightnode = []
    for x in nodeinfo :
        if x[0] < rootx :
            leftnode.append(x)
        else :
            rightnode.append(x)
    
    del dictionary[root]
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