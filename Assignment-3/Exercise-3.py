class TreeNode:
    def __init__(self, data):
        self.employees = []
        for i in data:
            self.employees.append(i)
        self.left = self.right = None
    

def NumberOfLevels(root):
    if not root:
        print("Error. Empty Tree.")
        return
    else:
        levelqueue = []
        levelqueue.append(root)
        levelcounter = 0
        
        while levelqueue:
        
            queuecount = len(levelqueue)
            levelcounter += 1 
            
            while queuecount > 0:
                
                nodetoprint = levelqueue.pop(0)
                
                if nodetoprint.left:
                    levelqueue.append(nodetoprint.left)
                if nodetoprint.right:
                    levelqueue.append(nodetoprint.right)
                    
                queuecount -= 1
               
            
        return "\nNumber of levels: " + str(levelcounter)
        
        
root = TreeNode([["Sarah", "CEO"], ["Jim", "Sales Rep"]])
root.left = TreeNode([["Pam", "Receptionist"], ["Selena", "Accounting"]])
root.right = TreeNode([["Creed", "I don't know"], ["Taylor", "Assistant"]])
root.left.left = TreeNode([["Michael", "Regional Managaer"], ["Adam", "IT"]])
root.left.right = TreeNode(["John", "Security"])
print(NumberOfLevels(root))
