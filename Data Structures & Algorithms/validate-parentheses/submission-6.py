class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        for i in s:
            if i=="[" or i=="{" or i=="(":
                stack.append(i)
            else:
                if stack ==[]:
                    return False
                if stack[-1] != pairs[i]:
                    return False
                stack.pop()
        return len(stack)==0