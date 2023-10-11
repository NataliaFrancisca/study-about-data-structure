from linkedListFunctions import printLL, createLinkedList;

elements = createLinkedList([1,2,3,4,5])

def deleteNode(head, position):
    current = head;
    prev = None;
    counter = 0;
    
    while(counter != position):
        if(current.next == None):
            print("This position doesn't exist")
            return;
        prev = current;
        current = current.next;
        counter+=1;
        
    if(prev == None):
        head = current.next;
    else:
        prev.next = current.next;
    
    printLL(head)

deleteNode(elements, 4);