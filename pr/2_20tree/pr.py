def preorder_traverse(T): # 전위순회
    if T:           # T is not None T는 방문 노드 정보
    # T가 존재하면 if문 실행 아니면 return
        visit(T)    # print(T.item)
        preorder_traverse(T.left)
        preorder_traverse(T.right)

def inorder_traverse(T):    # 중위순회
    if T:           # T is not None
        inorder_traverse(T.left)
        visit(T)                    # print(T.item)
        inorder_traverse(T.right)

def postorder_traverse(T):  # 후위순회
    if T:           # T is not None
        postorder_traverse(T.left)
        postorder_traverse(T.right)
        visit(T)                # print(T.item)

# 5번 노드의 조상 찾기
c = 5
while(a[c] != 0) # 루트인지 확인
    c = a[c]
    anc.append(c)   # 조상 목록
root = c