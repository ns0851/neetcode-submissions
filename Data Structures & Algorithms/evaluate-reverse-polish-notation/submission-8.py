class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif tokens[i] == '-':
                a = int(stack.pop())
                b=int(stack.pop())
                stack.append(b-a)
            elif tokens[i] == '*':
                ans = int(stack.pop()) * int(stack.pop())
                stack.append(ans)
            elif tokens[i]== '/':
                a = int(stack.pop())
                b=int(stack.pop())
                stack.append(b/a)
            else:
                stack.append(tokens[i])
            
        return int(stack[-1])
