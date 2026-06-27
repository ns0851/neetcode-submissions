class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top=-1
        if s[0]!='(' and s[0]!='[' and s[0]!='{':
            return False
        for i in s:
            if len(stack) > 0 and i=='}' and stack[top] == '{':
                stack.pop()
                top-=1
            elif len(stack) > 0 and i==')' and stack[top] == '(':
                stack.pop()
                top-=1
            elif len(stack) > 0 and i==']' and stack[top] == '[':
                stack.pop()
                top-=1
            else:
                if i not in '({[':
                    return False
                stack.append(i)
                top+=1
            
        return len(stack) == 0
