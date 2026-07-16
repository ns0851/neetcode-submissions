# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isValid = True
        self.check(root, float('-inf'), float('inf'))
        return self.isValid

    def check(self, root, low, high):
        if root is None:
            return
        if not (low < root.val < high):
            self.isValid = False
            return
        self.check(root.left, low, root.val)
        self.check(root.right, root.val, high)