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
        self.pivot = None
        node_inserted = node
        parent = node.parent

        while node != None:
            if node.balance >=1 or node.balance<=-1:
                if self.pivot is None:
                    self.pivot = node
            
            node.balance = self.calculate_balance(node)
            node = node.parent

            
        if self.pivot is None:
            print("Case 1: No pivot found")
        elif self.pivot is not None and (self.pivot.balance >= 1 or self.pivot.balance <= -1):
            print("Case 2: Pivot exists and the node was aded to the shorter subtree")

            if self.pivot.balance >1 and node_inserted.data<self.pivot.data:
                if parent.left == node_inserted:
                    parent.left == None
                else:
                    parent.right == None
                self.insert_to_shorter_subtree(node_inserted, 'left')
            elif self.pivot.balance<-1 and node_inserted.data> self.pivot.data:
                if parent.left == node_inserted:
                    parent.left == None
                else:
                    parent.right == None
                self.insert_to_shorter_subtree(node_inserted, 'right')


    def insert_to_shorter_subtree(self, node, subtree):
        current = self.pivot
        if subtree == 'left':
            current = current.left
        else:
            current = current.right
            
        while current is not None:
            parent = current
            if node.data <= current.data:
                current.balance -=1
                current = current.left
            else:
                current.balance +=1
                current = current.right


        if node.data <= parent.data:
            parent.left = node
        else:
            parent.right = node
        
        

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
    
    def _print_tree_recursive(self, node):
        if node is not None:
            # Print current node and its balance
            print(f"Node: {node.data}, Balance: {node.balance}")

            # Recursively print left subtree
            self._print_tree_recursive(node.left)

            # Recursively print right subtree
            self._print_tree_recursive(node.right)
def main():
    BST = binarySearchTree()
    BST.insert(1)
    BST.insert(2)
    BST.insert(3)
    BST.insert(5)
    BST.insert(4)

    BST._print_tree_recursive(BST.root)


if __name__ == '__main__':
    main()