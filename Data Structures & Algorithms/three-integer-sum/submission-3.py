class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range (0,len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            p1=i+1;
            p2=len(nums)-1
            while p1<p2:
                if nums[i]+nums[p1]+nums[p2] == 0:
                    result.append([nums[i],nums[p1],nums[p2]])
                    p1+=1
                    p2-=1

                    while p1 < p2 and nums[p1] == nums[p1-1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2+1]:
                        p2 -= 1
                elif nums[i]+nums[p1]+nums[p2] > 0:
                    p2-=1
                else:
                    p1+=1
        return result
                