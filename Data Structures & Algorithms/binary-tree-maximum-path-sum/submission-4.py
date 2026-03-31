# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float("-inf")
        def recurse(node: TreeNode):
            nonlocal result
            if not node:
                return 0
            max_left = max(0, recurse(node.left))
            max_right = max(0, recurse(node.right))
            result = max(result, node.val + max_left + max_right)
            return node.val + max(max_left, max_right)
        recurse(root)
        return result
                                                                                                                                    