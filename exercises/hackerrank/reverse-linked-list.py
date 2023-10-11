from linkedListFunctions import printLL, createLinkedList

# I WAS SUPER CRAZY DOING THIS; BUT WORKS ;) 
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

# THIS WAY IS BETTER 
def reverseLinkedList2(llist):
    current = llist;
    prev = None;
    
    while(current):
        next = current.next;
        current.next = prev;
        prev = current;
        current = next;
 
    printLL(prev);
 
elements = createLinkedList([1,2,3,4,5]);
reverseLinkedList(elements);

# current: 1; next: 2; 1.next = None; prev = 1; current = 2
# current: 2; next: 3; 2.next = 1; prev = 2-1; current = 3
# current: 3; next: 4; 3.next = 2; prev = 3-2-1; current = 4
# current: 4; next: 5; 4.next = 3; prev = 4-3-2-1; current = 5
