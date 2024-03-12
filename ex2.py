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
    
    def insert(self, data):
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
        
        
        self.update_balances(newnode)  

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
    
    def update_balances(self, node):
        while node != None:
            node.balance = self.calculate_balance(node)
            node = node.parent

    def calculate_balance(self,node):
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return right_height - left_height
    
    def height(self, node):
        if node is None:
            return -1
        else:
            height = -1
            stack = []  
            stack.append(node)
            stack.append(height)
            while len(stack)>0:
                current_height = stack.pop()
                current = stack.pop()
                if current is not None:
                    height = max(height, current_height)
                    stack.append(current.left)
                    stack.append(current_height + 1)
                    stack.append(current.right)
                    stack.append(current_height + 1)
            return height

