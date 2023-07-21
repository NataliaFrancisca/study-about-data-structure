class SinglyLinkedList:
    def __init__(self, data):
        self.data = data;
        self.next = None
        
class LinkedNode:
    def __init__(self):
        self.head = None;
    
    def append(self, value):
        node = self.head;
    
        if(self.head == None):
            self.head = SinglyLinkedList(value);
            return;
        
        while(node.next):
            node = node.next;
        
        node.next = SinglyLinkedList(value);
    
    def print(self):
        current = self.head;
        while(current):
            print(current.data)
            current = current.next;
    
        
node = LinkedNode();
values = [1,2,3,4]

for x in values:
    node.append(x);

node.print();