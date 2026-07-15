# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.queue = []
        self.final = []

        if root is None:
            return []

        self.queue.append(root)

        self.bfs(root)
        return self.final

    def bfs(self, root):
        while len(self.queue) > 0:
            self.final.append(self.queue[-1].val)
            snapshot = self.queue
            print(self.final)
            self.queue = []
            for i in snapshot:
                if i.left is not None:
                    self.queue.append(i.left)
                if i.right is not None:
                    self.queue.append(i.right)
        



