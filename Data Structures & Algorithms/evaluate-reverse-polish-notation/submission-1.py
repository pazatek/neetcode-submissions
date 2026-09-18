class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '*': 
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                divisor = stack.pop()
                value = stack.pop()
                stack.append(int(value / divisor))
            elif token == '-':
                remove = stack.pop()
                value = stack.pop()
                stack.append(value - remove)
            else:
                stack.append(int(token))
        return stack.pop()
            
            