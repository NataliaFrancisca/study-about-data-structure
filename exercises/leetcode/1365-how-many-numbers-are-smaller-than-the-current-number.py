def smallerNumbersThanCurrent(nums):
    counter = 0;
    smaller_arr = [];

    for x in nums:
        for b in nums:
            if(b < x):
                counter = counter + 1;
        smaller_arr.append(counter);
        counter = 0;
    print(smaller_arr);
    
    
smallerNumbersThanCurrent([8,1,2,2,3]);
smallerNumbersThanCurrent([1,2,4,6,3]);
