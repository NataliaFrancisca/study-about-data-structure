arr = [1,2,3,4,5,6];

def reverse(arr):
    right = len(arr) - 1;
    
    for i in range(int(len(arr) / 2)):
        left_element = arr[i];
        right_element = arr[right];
        
        arr[i] = right_element;
        arr[right] = left_element;
        
        right = right - 1;

    print(arr);
    
reverse([1,2]);
reverse([1,2,3]);
reverse([1,2,3,4]);
reverse([1,2,3,4,5]);
reverse([1,2,3,4,5,6]);
reverse([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])