class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        ans = None
        stack = []
        isOperator = False
        for i in range(len(tokens)):
            if tokens[i] == '+':
                ans = int(stack.pop()) + int(stack.pop())
                isOperator = True
            elif tokens[i] == '-':
                a = int(stack.pop())
                b=int(stack.pop())
                ans = b-a
                isOperator = True
            elif tokens[i] == '*':
                ans = int(stack.pop()) * int(stack.pop())
                isOperator = True
            elif tokens[i]== '/':
                a = int(stack.pop())
                b=int(stack.pop())
                ans = b/a
                isOperator = True
            
            if isOperator:
                stack.append(ans)
                isOperator = False
            else:
                stack.append(tokens[i])
            
        return int(ans)
