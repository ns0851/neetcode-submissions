class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)
        stack.append(0)

        for i in range(1,len(temperatures)):
            while len(stack)!=0 and (temperatures[i] > temperatures[stack[-1]]):
                output[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)
        return output