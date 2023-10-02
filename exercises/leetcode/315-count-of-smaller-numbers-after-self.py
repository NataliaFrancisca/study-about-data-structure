def countSmaller(arr:list):
    counter = 0;
    result = [];
    size = len(arr);
    
    for x in range(size):
        subarr = arr[x:size]
        for i in subarr:
            if(arr[x] > i):
                counter+=1;
        result.append(counter);
        counter = 0;
    print(result);

        
        
countSmaller([5,2,6,1]);
countSmaller([-1]);
countSmaller([-1,-1]);