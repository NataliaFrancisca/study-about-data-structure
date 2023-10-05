class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;

class LinkedList:
    def __init__(self):
        self.head = None;
    
    def append(self, value):
        if(self.head == None):
            self.head = Node(value);
            return;
        else:
            oldHead = self.head;
            self.head = Node(value);
            self.head.next = oldHead;
    
    def print(self):
        current = self.head;
        while(current):
            print(current.data);
            current = current.next;


values = [383, 484, 392, 975, 321]
linkedlist = LinkedList();
for i in values:
    linkedlist.append(i);
    
linkedlist.print();