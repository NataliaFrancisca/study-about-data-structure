# O(n)
def sum (target, arr):
    p1 = 0
    p2 = len(arr) - 1

    while(p1 < p2):
        sum = arr[p1] + arr[p2]
       
        if(sum > target):
            p2-=1

        if(sum < target):
            p1+=1

        if(sum == target):
           return [p1 + 1, p2 + 1]

sum(6, [1,1,1,2,3,3,4]) # [4,7]
sum(10, [2,4,4,6,8,9]) # [1,5]
sum(-1, [-1,0]) # [1,2]
sum(9, [2,7,11,15])  # [1,2]
sum(200, [3,24,50,79,88,150,345]) #[3,6]