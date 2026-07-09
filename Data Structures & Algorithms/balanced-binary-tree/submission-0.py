# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.check=0
        self.get_height(root)
        if self.check==0:
            return True
        return False
        
    def get_height(self, root):
        if not root:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)

        height = 1+max(left_height, right_height)
        if max(left_height, right_height) - min(left_height, right_height) > 1:
            self.check+=1
        return height
