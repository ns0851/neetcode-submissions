class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        while i < len(matrix):
            if(matrix[i][0] <= target and matrix[i][-1] >= target):
                for j in matrix[i]:
                    print(j)
                    if j == target:
                        return True
                i+=1
            else:
                i+=1
        return False