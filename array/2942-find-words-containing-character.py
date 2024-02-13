def findWordsContaining(array, target):
    indexes = [];
    
    for x in range(len(array)):
        for i in array[x]:
            if i == target:
                indexes.append(x);
                break;
    return indexes;

a = findWordsContaining(["leet","code"], "e");
b = findWordsContaining(["abc","bcd","aaaa","cbc"], "a");
c = findWordsContaining(["abc","bcd","aaaa","cbc"], "z");

print(a);
print(b);
print(c);
