from linkedListFunctions import printLL, createLinkedList

def reverseLinkedList(llist):
    current = llist;
    head = None;
    
    while(current.next):
        next = current.next;
        prev_head = head;
        
        if(head == None):
            head = next;
            next_current = next.next;
            current.next = next_current;
            head.next = current;
        else:            
            head = next;
            next_element_from_current = head.next; 
            current.next = next_element_from_current;

            head.next = prev_head;
    
    
    printLL(head);
 
 
elements = createLinkedList([1,2,3,4,5,6]);
reverseLinkedList(elements);