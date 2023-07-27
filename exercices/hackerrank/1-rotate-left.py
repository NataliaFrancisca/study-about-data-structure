def rotateLeft(d, arr): 
    while(d > 0):
        removedElement = arr.pop(0);
        arr.append(removedElement);
        d-=1;
    print(arr);
    
rotateLeft(2, [1,2,3,4,5]);