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

def main():
    arr = []
    times = []
    largest_abs_balances = []

    for i in range(1000):
        arr.append(i)

   

    for i in range(1000):
        random.shuffle(arr) # shuffling arr again
        BST = binarySearchTree()
        for num in arr:
            BST.insert(num)

        random_value = random.choice(arr)

        times.append(timeit.timeit(lambda: BST.search(random_value), number=10)/10)
        largest_abs_balances.append(BST.largest_balance())
        

    plt.scatter(largest_abs_balances, times)
    plt.title('Search time vs Absolute Balance')
    plt.xlabel('Absolute Balance')
    plt.ylabel('Search Time')
    plt.show()

if __name__ == '__main__':
    main()