# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_height = 0
        self.diameter = 0
        self.get_max(root)

        return self.diameter
        
    def get_max(self, root):
        if not root:
            return 0
        self.diameter = max(self.diameter, self.get_max(root.left) + self.get_max(root.right))
        return max(self.get_max(root.left), self.get_max(root.right))+1


        