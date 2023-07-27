class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data;
        self.next = None;

    
def insertNodeAtHead(llist, data):
    if(llist == None):
        llist = SinglyLinkedListNode(data);
    else:
        oldHead = llist;
        llist = SinglyLinkedListNode(data);
        llist.next = oldHead;
        
    return llist;
