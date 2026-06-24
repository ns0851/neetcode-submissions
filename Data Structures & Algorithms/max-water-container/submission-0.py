class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights)-1
        max_area = 0
        area = 0

        while p1<p2:
            if self.is_smallest(heights[p1], heights[p2]):
                area = heights[p1]*(p2-p1)
            else:
                area = heights[p2]*(p2-p1)
            
            if area > max_area:
                max_area = area
            if heights[p1] < heights[p2]:
                p1+=1
            else:
                p2-=1
        
        return max_area

    def is_smallest(self, p1, p2):
        if p1 > p2:
            return False
        else:
            return True
