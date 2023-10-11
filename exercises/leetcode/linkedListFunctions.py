def printLL(linkedList):
    current = linkedList;
    
    while(current):
        print(current.data);
        current = current.next;

class SinglyLinkedList:
    def __init__(self, data):
        self.data = data;
        self.next = None

def createLinkedList(values: list):
    elements = None;
    
    for x in values:
        if(elements == None):
            elements = SinglyLinkedList(x);
        else:
            current = elements;
            while(current.next):
                current = current.next;
            current.next = SinglyLinkedList(x);

    return elements;