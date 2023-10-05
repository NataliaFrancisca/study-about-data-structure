## CRAZY AND LONG WAY TO RESOLVE THE EXERCISE
# def numberOfGoodPairs(nums):
#     size = len(nums);
#     counter = 0;
#     goodPairsCounter = 0;
    
#     while(counter < size):
#         for i in range(counter + 1, size):
#             if(nums[counter] == nums[i]):
#                 goodPairsCounter+=1;
#         counter+=1;
#     print(goodPairsCounter);

def numberOfGoodPairs(nums):
    counter = 0;
    size = len(nums);
    
    for i in range(size):
        for n in range(i + 1, size):
            if(nums[i] == nums[n]):
                counter+=1;

    print(counter);

numberOfGoodPairs([1,2,3,1,1,3]);
# numberOfGoodPairs([1,1,1,1]);
# numberOfGoodPairs([[1,2,3]]);