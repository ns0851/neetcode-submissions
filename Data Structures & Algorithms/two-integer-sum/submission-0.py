class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exists = {}
        for i in range (0,len(nums)):
            if target-nums[i] in exists:
                return [exists[target-nums[i]],i]
            exists[nums[i]] = i