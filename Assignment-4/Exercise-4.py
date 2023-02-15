class TreeNode:
    def __init__(self, node):
        self.node = node
        self.left = self.right = None
        
    def insertNode(self, data):
        if self.node > data:
            if self.left:
                return self.left.insertNode(data)
            else:
                self.left = TreeNode(data)
                return "Added to the left"
        
        elif self.node < data:
            if self.right:
                return self.right.insertNode(data)
            else:
                self.right = TreeNode(data)
                return "Added to the right"
        
    def findNode(self, data):
        if self.node == data:
            return "Found it!"
        elif self.node > data:
            if self.left:
                return self.left.findNode(data) 
        elif self.node < data:
            if self.right:
                return self.right.findNode(data) 
        else:
            return "Not found:("
            
    def preorder(self):
        if self:
            print(self.node, end = "---")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    def postorder(self):
        if self:
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
        print(self.node, end = "---")
        
    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.node, end = "---")
            if self.right:
                self.right.inorder()
        

class Tree:
    def __init__(self):
        self.root = None
        
    def addtoTree(self, key):
        if self.root:
            return self.root.insertNode(key)
        else:
            self.root = TreeNode(key)
            return "added new Root!"
    
    def findNodeinTree(self, key):
        if self.root:
            return self.root.findNode(key)
        else:
            return "Error. Empty Tree."
    
    def preorderPrint(self):
        print("Preorder: ", end = " ")
        self.root.preorder()
        
    def inorderPrint(self):
        print("Inorder: ", end = " ")
        self.root.inorder()
        
    def postorderPrint(self):
        print("Postorder: ", end = " ")
        self.root.postorder()
        

BST1 = Tree()

print(BST1.addtoTree(1))
print(BST1.addtoTree(7))
print(BST1.addtoTree(17))
print(BST1.addtoTree(3))
print(BST1.addtoTree(6))
print()
BST1.preorderPrint()
print()
BST1.inorderPrint()
print()
BST1.postorderPrint()
