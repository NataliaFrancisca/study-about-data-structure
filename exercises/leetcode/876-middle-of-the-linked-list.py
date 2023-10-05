class SinglyLinkedList:
    def __init__(self, data):
        self.data = data;
        self.next = None

elements = None;

# CREATE THE NODE ELEMENTS IN THE LINKED LIST
for x in [1,2,3,4,5]:
# for x in [1,2,3,4,5,6]:
    if(elements == None):
        elements = SinglyLinkedList(x);
    else:
        current = elements;
        while(current.next):
            current = current.next;
        current.next = SinglyLinkedList(x);
      
def printLinkedList(list):
    current = list;
    
    while(current):
        print(current.data);
        current = current.next;      

# def middleOfLinkedList(list):
#     current = list;
#     counter = 0;
    
#     while(current):
#         counter+=1;
#         current = current.next;
    
#     middle = int(counter / 2);
#     current = list;
    
#     while(middle > 0):
#         current = current.next;
#         middle-=1;
    
#     printLinkedList(current);


## THIS IS VERY SMART, I SAW ON LEETCODE AND 🤯🤯🤯
def middleOfLinkedList(head):
    p = head;
    
    while(p and p.next):
        print("HEAD", head.data);
        print("P", p.next.data);
        head = head.next;
        p = p.next.next;

    printLinkedList(head);
    
middleOfLinkedList(elements);