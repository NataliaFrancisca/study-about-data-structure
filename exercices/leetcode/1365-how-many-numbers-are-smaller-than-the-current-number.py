def smallerNumbersThanCurrent(nums):
    smaller = [];
    index = 0;
    counter = 0;
    # for x in nums:
    #     for i in nums[x, len(nums)]:
    #         print(x, i)
    for i in range(len(nums)):
        for x in range(len(nums)):
            index = i;
            print(nums[i], nums[x])
            if(nums[x] < nums[i]):
                counter+=1;
            if(i != index):
                index = i;
                smaller.append(counter);
                counter = 0;
    
    print(smaller)
smallerNumbersThanCurrent([8,1,2,2,3]);