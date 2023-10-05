def removeDuplicates(nums):
    i = 0;
    
    while(i < len(nums) - 1):
        if(nums[i] == nums[i + 1]):
            nums.pop(i);
        else:
            i+=1;

    print(len(nums));
 
    
# removeDuplicates([1,1,2]);
removeDuplicates([0,0,1,1,1,2,2,3,3,4]);