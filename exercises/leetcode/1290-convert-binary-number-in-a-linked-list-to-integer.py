from linkedListFunctions import printLL, createLinkedList

def getDecimalValue(list):
    arr = [];
    current = list;

    
    while(current):
        arr.append(current.data);
        current = current.next;

    size = len(arr) - 1;
    result = 0;
    
    for i in range(len(arr)):
        value = 2 ** size * arr[i];
        result+=value;
        size-=1;

    print(result);
    
    
values = createLinkedList([1,0,1]);
getDecimalValue(values);