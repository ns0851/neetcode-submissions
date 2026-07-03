class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        while i < len(matrix):
            if(matrix[i][0] <= target and matrix[i][-1] >= target):
                for j in matrix[i]:
                    if j == target:
                        return True
                return False
            else:
                i+=1
        return False