class AVLNode:
    def __init__(self, newItem, left, right, h):
        self.item = newItem
        self.left = left
        self.right = right
        self.height = h

class AVLTree:
    def __init__(self):
        self.NIL = AVLNode(None, None, None, 0)
        self.__root = self.NIL
        self.LL = 1; self.LR = 2; self.RR = 3; self.RL = 4
        self.NO_NEED = 0
        self.ILLEGAL = -1
    
    # [알고리즘 10-1] 구현: 검색
    def search(self, x):
        return self.__searchItem(self.__root, x)
    
    def __searchItem(self, tNode:AVLNode, x) -> AVLNode:
        if (tNode == self.NIL):
            return self.NIL
        elif (x == tNode.item):
            return tNode
        elif x < tNode.item:
            return self.__searchItem(tNode.left, x)
        else:
            return self.__searchItem(tNode.right, x)
        
    # [알고리즘 10-3] 구현: 삽입
    def insert(self, x):
        self.__root = self.__insertItem(self.__root, x)

    def __insertItem(self, tNode:AVLNode, x) -> AVLNode:
        if (tNode == self.NIL): # 루트 노드가 리프일 경우 삽입
            tNode = AVLNode(x, self.NIL, self.NIL, 1)
        elif (x < tNode.item):  # x가 작을 경우 왼자식으로
            tNode.left = self.__insertItem(tNode.left, x)   # 현재 tNode는 변함없이 tNode.left를 루트 노드로 재귀호출
            tNode.height = 1 + max(tNode.right.height, tNode.left.height) # 삽입 후 높이 수정 (tNode 높이 = 자식들 중 큰 거+1)
            type = self.__needBalance(tNode)    # 밸런스 체크
            if (type != self.NO_NEED):
                tNode = self.__balanceAVL(tNode, type)
        else:
            tNode.right = self.__insertItem(tNode.right, x)
            tNode.height = 1 + max(tNode.right.height, tNode.left.height)
            type = self.__needBalance(tNode)
            if (type != self.NO_NEED):
                tNode = self.__balanceAVL(tNode, type)
        return tNode
    
    # [알고리즘 10-7] 구현: 삭제
    def delete(self, x):
        self.__root = self.__deleteItem(self.__root, x)

    def __deleteItem(self, tNode:AVLNode, x) -> AVLNode:
        if tNode == self.NIL: # x가 존재하지 않을 때
            return self.NIL
        else:
            if (x == tNode.item):   # x 찾았을 때
                tNode = self.__deleteNode(tNode) # tNode 삭제
            elif (x < tNode.item):  # x가 tNode.item보다 작을 때
                tNode.left = self.__deleteItem(tNode.left, x) # tNode.left에서 삭제 수행
                tNode.height = 1 + max(tNode.right.height, tNode.left.height) # 삭제 후 높이 수정
                type = self.__needBalance(tNode) # 밸런스 체크
                if (type != self.NO_NEED):
                    tNode = self.__balanceAVL(tNode, type)
            else:
                tNode.right = self.__deleteItem(tNode.right, x)
                tNode.height = 1 + max(tNode.right.height, tNode.left.height)
                type = self.__needBalance(tNode)
                if (type != self.NO_NEED):
                    tNode = self.__balanceAVL(tNode, type)
            return tNode
    
    def __deleteNode(self, tNode:AVLNode) -> AVLNode:
        # case1: tNode가 리프노드
        if (tNode.left == self.NIL and tNode.right == self.NIL):
            return self.NIL
        # case2: tNode의 자식이 하나일 경우
        elif (tNode.left == self.NIL):
            return tNode.right
        elif (tNode.right == self.NIL):
            return tNode.left
        # case3: tNode의 자식이 둘일 경우 (우서브 트리에서 가장 작은 item)
        else:
            (rtnItem, rtnNode) = self.__deleteMinItem(tNode.right)
            tNode.item = rtnItem
            tNode.right = rtnNode
            tNode.height = 1 + max(tNode.right.height, tNode.left.height)
            type = self.__needBalance(tNode)
            if (type != self.NO_NEED):
                tNode = self.__balanceAVL(tNode, type)
            return tNode
        
    def __deleteMinItem(self, tNode:AVLNode) -> tuple:
        if (tNode.left == self.NIL):
            return (tNode.item, tNode.right)
        else: # 오른자식을 왼자식으로 만드는 작업
            (rtnItem, rtnNode) = self.__deleteMinItem(tNode.left)
            tNode.left = rtnNode
            tNode.height = 1 + max(tNode.right.height, tNode.left.height)
            type = self.__needBalance(tNode)
            if (type != self.NO_NEED):
                tNode = self.__balanceAVL(tNode, type)
            return (rtnItem, tNode) ## orginal (tNode, rtnItem)
    
    # Balance 체크
    def __needBalance(self, t:AVLNode) -> int:
        type = self.ILLEGAL
        if (t.left.height + 2 <= t.right.height):
            if (t.right.left.height <= t.right.right.height):
                type = self.RR
            else:
                type = self.RL
        elif (t.left.height >= t.right.height + 2):
            if (t.left.left.height >= t.left.right.height):
                type = self.LL
            else:
                type = self.LR
        else:
            type = self.NO_NEED
        return type

    def __balanceAVL(self, tNode:AVLNode, type:int) -> AVLNode:
        rtnNode = self.NIL
        if (type == self.LL):
            rtnNode = self.__rightRotate(tNode)
        elif (type == self.LR):
            tNode.left = self.__leftRotate(tNode.left)
            rtnNode = self.__rightRotate(tNode)
        elif (type == self.RR):
            rtnNode = self.__leftRotate(tNode)
        elif (type == self.RL):
            tNode.right = self.__rightRotate(tNode.right)
            rtnNode = self.__leftRotate(tNode)
        else:
            print("Impossible type!")
        return rtnNode
    
    # [알고리즘 11-1] 구현: 죄회전, 우회전
    def __leftRotate(self, t:AVLNode) -> AVLNode:
        RChild = t.right
        if RChild == self.NIL:
            print(t.item, "'s RChild shouldn't be NIL!")
        RLChild = RChild.left
        RChild.left = t
        t.right = RLChild
        t.height = 1 + max(t.left.height, t.right.height)
        RChild.height = 1 + max(RChild.left.height, RChild.right.height)
        return RChild
    
    def __rightRotate(self, t:AVLNode) -> AVLNode:
        LChild = t.left
        if (LChild == self.NIL):
            print(t.item, "'s LChild shouldn't be NIL!")
        LRChild = LChild.right
        LChild.right = t
        t.left = LRChild
        t.height = 1 + max(t.left.height, t.right.height)
        LChild.height = 1 + max(LChild.left.height, LChild.right.height)
        return LChild
    
    # 기타
    def isEmpty(self) -> bool:
        return self.__root == self.NotImplemented
    
    def clear(self):
        self.__root = self.NIL

    # 전위순회
    def pre_order_traverse(self):
        self.__pre_order_traverse(self.__root)

    def __pre_order_traverse(self, tNode:AVLNode):
        if (tNode != None):
            print(tNode.item, end = ' ')
            self.__pre_order_traverse(tNode.left)
            self.__pre_order_traverse(tNode.right)

    # 중위순회
    def in_order_traverse(self):
        self.__in_order_traverse(self.__root)
    
    def __in_order_traverse(self, tNode:AVLNode):
        if (tNode != None):
            self.__in_order_traverse(tNode.left)
            print(tNode.item, end = ' ')
            self.__in_order_traverse(tNode.right)
    
    # 후위순회
    def post_order_traverse(self):
        self.__post_order_traverse(self.__root)

    def __post_order_traverse(self, tNode:AVLNode):
        if (tNode != None):
            self.__post_order_traverse(tNode.left)
            self.__post_order_traverse(tNode.right)
            print(tNode.item, end = ' ')
