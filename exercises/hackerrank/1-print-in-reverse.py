class SinglyLinkedList:
    def __init__(self, data):
        self.data = data;
        self.next = None
   
elements = None;

# CREATE THE NODE ELEMENTS IN THE LINKED LIST
for x in [2,3,4,5]:
    if(elements == None):
        elements = SinglyLinkedList(x);
    else:
        current = elements;
        while(current.next):
            current = current.next;
        current.next = SinglyLinkedList(x);
         
def printInReverse(arr):
    current = arr;
    dumbNode = None;
    
    while(current):
        if(dumbNode == None):
            dumbNode = SinglyLinkedList(current.data);
        else:
            prev = dumbNode;
            dumbNode = SinglyLinkedList(current.data);
            dumbNode.next = prev;
        current = current.next;
    
    current = dumbNode; 
    while(current):
        print(current.data);
        current = current.next;
   
    
def printInReverse2(arr):
    current = arr;
    prev = None;
    
    while(current):
        next = current.next;
        current.next = prev;
        prev = current;
        current = next;
    
    while(prev):
        print(prev.data);
        prev = prev.next;



printInReverse(elements);
printInReverse2(elements);