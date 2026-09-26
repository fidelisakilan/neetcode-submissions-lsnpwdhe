# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        temp1 = root.left
        temp2 = root.right
        root.left = temp2
        root.right = temp1

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root