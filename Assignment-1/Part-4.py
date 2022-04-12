class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next_ = None
        
    
class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.n = 0
        
    def push(self, new_data):
        newNode = LinkedNode(new_data)
        
        if self.head is None:
            self.head = newNode
            self.n += 1
            return
        
        else:
            tail = self.head
            while (tail.next_):
                tail = tail.next_
                
            tail.next_ = newNode
        self.n += 1
        
    def insertAfter(self, new_data, prev_node):
        
        if prev_node is None:
            print("Error: Not possible.")
            return
        
        newNode = LinkedNode(new_data)
        newNode.next_ = prev_node.next_
        prev_node.next_ = newNode
        self.n += 1
    
    def size(self):
        return self.n
        
    def isEmpty(self):
        return (self.head is None)
        
    def printList(self):
        last = self.head
        while (last):
            print(last.data, end = "-->")
            last = last.next_
    
    def pop(self):
        if self.head is None:
            print("Error: Linked List is empty.")
            return
        
        else:
            tail = self.head
            while (tail.next_.next_):
                tail = tail.next_
                
            tail.next_ = None
        self.n -= 1

        
    def remove(self, index_to_delete):
        
        last = self.head
        i = 0
        
        while(last.next_):
            if self.head is None:
                print("Error: Empty List.")
                return 
            elif index_to_delete > self.n:
                print("Error: Index out of range.")
                return
            elif i == index_to_delete:
                old = last
                last = last.next_.next_
                self.n -= 1
                return old
            else:
                last = last.next_
                i += 1
        
                
    def elementAt(self, index):
        
        temp = self.head
        i = 0
        
        while (temp):
            if self.head is None:
                print("Error: Empty List.")
                break
            elif index > self.n:
                print("Error: Index out of range.")
                break
            elif (i == index):
                return temp.data
            else:
                temp = temp.next_
                i += 1
        
        
            
llist = LinkedList()
 
    # Insert 6.  So linked list becomes 6->None
llist.push(6)
 
    # Insert 7 at the end. So linked list becomes 7->6->None
llist.push(7);
 
    # Insert 1 at the end. So linked list becomes 1->7->6->None
llist.push(1);
 
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
llist.push(4)

llist.insertAfter(8, llist.head.next_)
llist.printList()
print()

llist.insertAfter(1, llist.head)
llist.printList()
print()

llist.insertAfter(3, llist.head.next_.next_.next_)



print(llist.size())
llist.printList()
print()
print()

llist.pop()
llist.printList()
print()
print()

print(llist.elementAt(2))
