class Solution:
    def findMin(self, nums: List[int]) -> int:
        maxi = len(nums)-1
        mini = 0

        while mini<maxi:
            mid = (maxi+mini)//2
            if nums[mid]>nums[maxi]:
                mini = mid+1
            else:
                maxi = mid
        return nums[mini]
