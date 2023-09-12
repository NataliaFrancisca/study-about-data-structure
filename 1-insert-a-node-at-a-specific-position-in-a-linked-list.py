class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;

class LinkedList:
    def __init__(self):
        self.head = None;
        self.tail = None;
        
    def appendIndex(self, value, index):
        current = self.head;
        prev = self.head;
        counter = 0;
        
        while(current):
            if(counter == index):
                prev.next = Node(value);
                prev.next.next = current;
            counter = counter + 1;
            prev = current;
            current = current.next;
    
    def append(self, value):
        if(self.head == None):
            self.head = Node(value);
            self.tail = Node(value);
            return;
        else:
            self.head.next = self.tail;
            self.tail.next = Node(value);
            self.tail = Node(value)
    def print(self):
        current = self.head;
        while(current):
            print(current.data);
            current = current.next;
    


values = [16, 13, 7]
linkedList = LinkedList();
for i in values:
    linkedList.append(i);
    
linkedList.appendIndex(1, 20);
linkedList.print();