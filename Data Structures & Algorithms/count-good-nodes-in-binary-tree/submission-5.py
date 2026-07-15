# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        self.dfs(root, float('-inf'))
        return self.count
        
    def dfs(self, root,max_so_far):
        if root is None:
            return
        if root.val >= max_so_far:
            self.count+=1
            max_so_far = root.val

        self.dfs(root.left, max_so_far)
        self.dfs(root.right, max_so_far)