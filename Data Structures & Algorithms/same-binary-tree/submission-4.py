# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isSame = True
        self.check(p,q)

        return self.isSame
    
    def check(self, p, q):
        if p != None and q != None and p.val!=q.val:
            self.isSame = False
        if (p==None and q!=None) or (p!=None and q==None):
            self.isSame = False
        if p and q:
            self.check(p.left, q.left)
            self.check(p.right, q.right)
        else:
            return

        