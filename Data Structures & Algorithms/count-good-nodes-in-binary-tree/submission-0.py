# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        max_val = float('-inf')

        def dfs(node, max_val):
            nonlocal good;
            if not node:
                return
            if node.val >= max_val:
                max_val = node.val
                good += 1

            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root, float('-inf'))
        return good

        