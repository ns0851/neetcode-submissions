# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.maxi = max(p.val,q.val)
        self.mini = min(p.val,q.val)

        return self.check(root)

    def check(self,root):
        if not root:
            return
        if root.val > self.maxi and root.val > self.mini:
            # return left
            return self.check(root.left)
        elif root.val < self.maxi and root.val > self.mini:
            # return it
            return root
        elif root.val==self.maxi:
            return root
        elif root.val == self.mini:
            return root
        else:
            # return right
            return self.check(root.right)