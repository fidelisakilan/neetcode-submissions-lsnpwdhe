# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_count = 0
        def recurse(node: TreeNode, target):
            nonlocal good_count
            if not node:
                return None
            if node.val >= target:
                good_count += 1
            recurse(node.left, max(target, node.val))
            recurse(node.right, max(target, node.val))
            return recurse
        
        recurse(root, -200)


        return good_count
        