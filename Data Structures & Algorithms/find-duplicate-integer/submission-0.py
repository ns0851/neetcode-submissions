class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c={}
        for i in nums:
            c[i] = c.get(i,0)+1
        print(c)
        for i in c:
            if c[i]>1:
                return i