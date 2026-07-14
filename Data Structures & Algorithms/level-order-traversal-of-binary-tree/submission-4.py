# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.queue = []
        self.order = []
        if root is None:
            return []
        self.queue.append(root)

        self.bfs(root)

        return self.order

    
    def bfs(self, root):
        while len(self.queue) > 0:
            leng = len(self.queue)
            level_nodes = self.queue[:leng]
            self.order.append([node.val for node in level_nodes])
            self.queue = []
            for i in level_nodes:
                if i.left is not None:
                    self.queue.append(i.left)
                if i.right is not None:
                    self.queue.append(i.right)


