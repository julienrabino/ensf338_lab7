import random
import timeit
import matplotlib.pyplot as plt
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
                print("Case 1: No pivot found")
        else:
            if pivot_balance >=1:
                if node_inserted.data<self.pivot.data and setup == 0:
                    print("Case 2: Pivot exists and the node was added to the shorter subtree")
                elif node_inserted.data>self.pivot.data and setup == 0:
                    print("Case 3: not supported")


            elif pivot_balance<=-1:
                if node_inserted.data>self.pivot.data and setup == 0:
                    print("Case 2: Pivot exists and the node was added to the shorter subtree")
                elif node_inserted.data<self.pivot.data and setup == 0:
                    print("Case 3: not supported")
                
         


        

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
    
    # def _print_tree_recursive(self, node):
    #     if node is not None:
    #         # Print current node and its balance
    #         print(f"Node: {node.data}, Balance: {node.balance}")

    #         # Recursively print left subtree
    #         self._print_tree_recursive(node.left)

    #         # Recursively print right subtree
    #         self._print_tree_recursive(node.right)
def main():

    # 4a) Adding a node results in case 1
    BST = binarySearchTree()

    BST.insert(10, 1)
    BST.insert(8,1)
    BST.insert(11,1)

    print("Message from BST after insertion of node: ")
    BST.insert(6,0)



    # 4b) Adding a node results in case 2
    BST = binarySearchTree()
    BST.insert(10,1)
    BST.insert(12,1)
    BST.insert(13,1)
    BST.insert(9,1)
    print("Message from BST after insertion of node: ")
    BST.insert(8,0)

    # 4c) Adding a node results in case 3
    BST = binarySearchTree()
    BST.insert(8,1)
    BST.insert(9,1)
    BST.insert(10,1)
    BST.insert(11,1)
    print("Message from BST after insertion of node: ")
    BST.insert(12,0)

if __name__ == '__main__':
    main()