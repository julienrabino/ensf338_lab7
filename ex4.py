class Node:
    def __init__(self,data, parent = None, left = None, right = None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        self.balance = 0
    

class binarySearchTree:
    def __init__(self):
        self.root = None
        self.pivot = None

    def insert(self, data, setup):
        current = self.root

        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right
        

        newnode = Node(data, parent)    
        if parent is None:
            self.root = newnode
        elif data <= parent.data:
            parent.left = newnode
        else:
            parent.right = newnode
        
        
        self.update_balances(newnode,setup)  

        return newnode
    
    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return current
            elif data <= current.data:
                current = current.left
            else:
                current = current.right
        return None
    
    def update_balances(self, node, setup):
        self.pivot = None
        node_inserted = node
        parent = node.parent
        pivot_balance = 0

        while node != None:
            if node.balance >=1 or node.balance<=-1:
                if self.pivot is None:
                    self.pivot = node
                    pivot_balance = node.balance
                    # if setup == 0:
                    #     print("Case 2: Pivot exists and the node was added to the shorter subtree")
            node.balance = self.calculate_balance(node)
            node = node.parent

            
        if self.pivot is None:
            if setup == 0:
                print("Case 1 -  No pivot found")
        else:
            if pivot_balance >=1:
                if node_inserted.data<self.pivot.data and setup == 0:
                    print("Case 2 -  Pivot exists and the node was added to the shorter subtree")
                elif node_inserted.data>self.pivot.data and setup == 0:
                    if node_inserted.data>self.pivot.right.data:
                        self.left_rotate(self.pivot)
                        print("Case 3a - adding a node to an outside subtree")
                    else:
                        self._rl_rotate(self.pivot)
                        print("Case 3b - adding a node to an inside subtree")


            elif pivot_balance<=-1:
                if node_inserted.data>self.pivot.data and setup == 0:
                    print("Case 2 - Pivot exists and the node was added to the shorter subtree")
                elif node_inserted.data<self.pivot.data and setup == 0:
                    if node_inserted.data<self.pivot.left.data:
                        self.right_rotate(self.pivot)
                        print("Case 3a - adding a node to an outside subtree")
                    else:
                        self._lr_rotate(self.pivot)
                        print("Case 3b - adding a node to an inside subtree")
                
    def calculate_balance(self,node):
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return right_height - left_height
    
    def height(self, node):
        if node is None:
            return 0
    
        queue = [node]
        height = 0
    
        while len(queue)>0:
            size = len(queue)
        
            for i in range(size):
                current = queue.pop(0)
            
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        
            height += 1
    
        return height

    def largest_balance(self):
        if self.root is None:
            return 0 
        
        balance_list = []
        
        stack = [self.root]
        
        while len(stack)>0:
            node = stack.pop()
            balance = abs(node.balance)
            balance_list.append(balance)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        max_balance = max(balance_list)
        
        return max_balance
    
    def left_rotate(self, node): # node refers to the ancestor node
        pivot = node.right
        son = pivot.right
        temp = pivot # store pivot and its subtree into temp variable
        node.right = son # right pointer of ancestor points to son
        if son:
            son.parent = node
        temp.right = son.left
        if son.left:
            son.left.parent = temp
        son.left = temp
        temp.parent = son

    def right_rotate(self, node):
        pivot = node.left
        son = pivot.left
        temp = pivot
        node.left = son
        if son:
            son.parent = node
        temp.left = son.right
        if son.right:
            son.right.parent = temp
        son.right = temp
        temp.parent = son
        
    def _lr_rotate(self, pivot):
        ancestor = pivot.parent
        son = pivot.left
        grandson = son.right
        # left rotation at grandson
        pivot.left = grandson
        if grandson.left is not None:
            son.right = grandson.left
            grandson.left = son
        # right rotation around grandson
        if ancestor is None:
            self.root = grandson
        elif pivot.data < ancestor.data:
            ancestor.left = grandson
        else:
            ancestor.right = grandson
        if grandson.right is not None:
            pivot.left = grandson.right
        grandson.right = pivot

    def _rl_rotate(self, pivot):
        ancestor = pivot.parent
        son = pivot.right
        grandson = son.left
        # right rotation at grandson
        pivot.right = grandson
        if grandson.right is not None:
            son.left = grandson.right
            grandson.right = son
        # left rotation around grandson
        if ancestor is None:
            self.root = grandson
        elif pivot.data > ancestor.data:
            ancestor.right = grandson
        else:
            ancestor.left = grandson
        if grandson.left is not None:
            pivot.right = grandson.left
        grandson.left = pivot


# 4. Create two extra test cases, both testing case 3b (now the code should
# not return an error!) [0.2 pts]

def main():

    #Adding a node results in case 1
    BST = binarySearchTree()

    BST.insert(10, 1)
    BST.insert(8,1)
    BST.insert(11,1)

    print("Message from BST after insertion of node: " ,end = '')
    BST.insert(6,0)



    #Adding a node results in case 2
    BST = binarySearchTree()
    BST.insert(10,1)
    BST.insert(12,1)
    BST.insert(13,1)
    BST.insert(9,1)
    print("Message from BST after insertion of node: ", end= '')
    BST.insert(8,0)

    #Adding a node results in case 3a
    BST = binarySearchTree()
    BST.insert(8,1)
    BST.insert(9,1)
    BST.insert(10,1)
    BST.insert(11,1)
    print("Message from BST after insertion of node: ", end='')
    BST.insert(12,0)

    #Adding a node results in case 3b
    BST = binarySearchTree()
    BST.insert(5,1)
    BST.insert(3,1)
    BST.insert(8,1)
    BST.insert(7,1)
    BST.insert(13,1)
    print("Message from BST after insertion of node: ", end='')
    BST.insert(6,0)

    #Adding a node results in case 3b
    BST = binarySearchTree()
    BST.insert(15,1)
    BST.insert(9,1)
    BST.insert(17,1)
    BST.insert(7,1)
    BST.insert(12,1)
    print("Message from BST after insertion of node: ", end='')
    BST.insert(13,0)


if __name__ == '__main__':
    main()
       
