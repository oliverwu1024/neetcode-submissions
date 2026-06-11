class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if i!="+" and i!="C" and i!="D":
                stack.append(int(i))
            
            if i == "+":
                stack.append(stack[-1]+stack[-2])            
            if i == "C":
                stack.pop()
            if i== "D":
                stack.append(stack[-1] * 2)
        return sum(stack)