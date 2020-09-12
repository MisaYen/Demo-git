class Node():
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.Right = None
        
    def insert(self,data):
        if self.data :
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else :
                    self.left = Node(data)
            else :
                if self.Right:
                    self.Right.insert(data)
                else :
                    self.Right = Node(data)
        else :
            self.data = data
            
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.Right:
            self.Right.inorder()

class Delete_Node():
    def deleteNode(self,root,key):
        if root is None:
            return None
        if key < root.data:
            root.left = self.deleteNode(root.left,key)
            return root
        if key > root.data:
            root.Right = self.deleteNode(root.Right,key)
            return root
        if root.left is None:
            return root.Right
        if root.Right is None:
            return root.left
        succ = self.max_node(root.left)
        tmp = Node(succ.data)
        tmp.left = self.left_node(root.left) 
        tmp.Right = root.Right 
        
    def max_node(self,node):
        while node.Right:
            node = node.Right
        return node
    
    def left_node(self,node):
        if node.Right is None:
            new_root = node.left 
            return new_root
        node.Right = self.left_node(node.Right)
        return node
tree = Node()
list1 = [5,12,6,89,21,54,32,54,20,3,41]
for i in list1:
    tree.insert(i)
tree.inorder()
