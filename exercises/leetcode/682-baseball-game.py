from ast import List
# ops = ["5","2","C","D","+"]
ops = ["1","C"];

class Solution:
    def calPoints(self, operations) -> int:
        self.operations = operations
        self.value = []
        self.finalResult = 0

        for x in self.operations:
            if x == "C":
                self.value.pop()
            elif x == "D":
                mult = self.value[-1] * 2;
                self.value.append(mult);
            elif x == "+":
                sum = int(self.value[-1]) + int(self.value[-2])
                self.value.append(sum);
            else:
                self.value.append(int(x))
            
        for i in self.value:
            self.finalResult += i;
        
        return self.finalResult

    
result = Solution();
result.calPoints(ops);
print(result.finalResult);
