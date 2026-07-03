import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = max(piles)  
        mini = 1
        min_mid = float('inf')
        k=0

        while mini <= maxi:
            mid = (mini+maxi)//2
            for i in piles:
                k+=math.ceil(i/mid)
            if k<h:
                min_mid = min(min_mid,mid)
                print(k,h,mid)
                maxi = mid-1
            elif k>h:
                mini = mid+1
            else:
                min_mid = min(min_mid,mid)
                maxi = mid-1

            k=0
        return min_mid            