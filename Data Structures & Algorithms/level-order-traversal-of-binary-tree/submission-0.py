# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([root])
        res = []

        while q:
            curr = []
            for _ in range(len(q)):
                value = q.popleft()
                curr.append(value.val)
                if value.left: q.append(value.left)
                if value.right: q.append(value.right)
            res.append(curr)
        return res

        