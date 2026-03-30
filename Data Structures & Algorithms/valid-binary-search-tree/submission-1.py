# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def recurse(node: TreeNode, min_val: float, max_val: float):
            if not node:
                return True
            if min_val < node.val < max_val:
                return recurse(node.left, min_val, node.val) and recurse(node.right, node.val, max_val)
            else:
                return False

        return recurse(root, float("-inf"), float("inf"))

        
        