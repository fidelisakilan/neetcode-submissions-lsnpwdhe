# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

maxVal = 0

class Solution:

    def recurse(self, root: TreeNode):
        global maxVal
        if root is None:
            return 0
        return 1 + max(self.recurse(root.left), self.recurse(root.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return self.recurse(root)
        