def removeElement(arr, element):
    i = 0;
    
    while(i < len(arr)):
        if(arr[i] == element):
            arr.pop(i);
        else:
            i+=1;
   
    print(arr);
    
# removeElement([3,2,1,3], 3);
removeElement([0,1,2,2,3,0,4,2], 2);