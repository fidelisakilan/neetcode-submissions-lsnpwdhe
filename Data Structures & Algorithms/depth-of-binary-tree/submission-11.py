# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def recurse(node, height):
            nonlocal res
            if not node:
                return None
            res = max(res, height)
            recurse(node.left, height+1)
            recurse(node.right, height+1)

        recurse(root, 1)
        return res