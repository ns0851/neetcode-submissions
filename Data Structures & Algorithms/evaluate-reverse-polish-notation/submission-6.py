class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = None
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                ans = int(stack.pop()) + int(stack.pop())
                stack.append(ans)
            elif tokens[i] == '-':
                a = int(stack.pop())
                b=int(stack.pop())
                ans = b-a
                stack.append(ans)
            elif tokens[i] == '*':
                ans = int(stack.pop()) * int(stack.pop())
                stack.append(ans)
            elif tokens[i]== '/':
                a = int(stack.pop())
                b=int(stack.pop())
                ans = b/a
                stack.append(ans)
            else:
                stack.append(tokens[i])
            
        return int(stack[-1])
