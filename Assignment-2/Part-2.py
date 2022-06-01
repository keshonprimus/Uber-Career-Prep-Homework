class TreeNode:
    def __init__(self, data):
        self.employees = []
        for i in data: #accepts an array of data input
            self.employees.append(i)
        self.left = self.right = None
    

def printbyLevel(root):
    if not root:
        print("Error. Empty Tree.")
        return
    else:
        levelqueue = []
        levelqueue.append(root)
        levelcounter = 1
        
        while levelqueue:
        
            queuecount = len(levelqueue)
            
            print("\nLevel", levelcounter, end = "")
            print(":", sep = "")
            
            while queuecount > 0:
                
                nodetoprint = levelqueue.pop(0)
                
                for i in range(0, len(nodetoprint.employees), 1):
                    if len(nodetoprint.employees) > 1:
                        print("Name:", nodetoprint.employees[i][0], end = ", ")
                        print("Title:", nodetoprint.employees[i][1])    
                        
                    else:    
                        print("Name:", nodetoprint.employees[0], end = ", ")
                        print("Title:", nodetoprint.employees[1])
                        
                
                if nodetoprint.left:
                    levelqueue.append(nodetoprint.left)
                if nodetoprint.right:
                    levelqueue.append(nodetoprint.right)
                    
                queuecount -= 1
            levelcounter += 1    
            
            
root = TreeNode([["Sarah", "CEO"], ["Jim", "Sales Rep"]])
root.left = TreeNode([["Pam", "Receptionist"], ["Selena", "Accounting"]])
root.right = TreeNode([["Creed", "I don't know"], ["Taylor", "Assistant"]])
root.left.left = TreeNode([["Michael", "Regional Managaer"], ["Adam", "IT"]])
root.left.right = TreeNode(["John", "Security"])
printbyLevel(root)
