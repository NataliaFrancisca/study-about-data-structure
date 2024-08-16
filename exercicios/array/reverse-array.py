arr = [1,2,3,4,5]
arr2 = [5,4,3,2,1]
arr3 = [1,2,3,4,5,6]

def reverse(arr):
    p1 = 0
    p2 = len(arr) - 1

    actions = round(len(arr) / 2);

    while(actions > 0):
        prev = { p1: arr[p1], p2: arr[p2] }

        arr[p1] = prev[p2]
        arr[p2] = prev[p1]

        p1+=1;
        p2-=1;
    
        actions-=1
    
    print(arr)

reverse(arr)
reverse(arr2)
reverse(arr3)