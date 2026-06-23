class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        is_zero = 0
        resultant = []
        result = 0
        for i in nums:
            if(i!=0):   
                total_product *= i
            else:
                is_zero +=1
        if is_zero>=2:
            return [0]*len(nums)
        for i in nums:
            if is_zero > 0:
                if i==0:
                    resultant.append(total_product)
                else:
                    resultant.append(0)
            else:
                resultant.append(total_product//i)
        return resultant