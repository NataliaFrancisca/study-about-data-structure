arr = [1,3,2,1];

def getConcatenation(arr):
    arr_size = len(arr);
    
    for x in range(arr_size):
        arr.append(arr[x]);
    
    return arr;
    
result = getConcatenation(arr);
print(result);

# A ANSWER THAT I SAW AT LEETCODE - easy right???
def getConcatenation1(arr):
    return arr + arr;

result1 = getConcatenation1(arr);
print(result1);