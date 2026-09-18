class Solution:
    def isValid(self, s: str) -> bool:
        d = {")": "(", "]": "[", "}": "{"}
        stack = []

        for bracket in s:
            if bracket in d: # if it's a closer
                if not stack: # check if stack is empty 
                    return False
                if stack.pop() != d[bracket]:
                    return False            
            else:            # if it's an opener
                stack.append(bracket) # add it to our stack
        return not stack