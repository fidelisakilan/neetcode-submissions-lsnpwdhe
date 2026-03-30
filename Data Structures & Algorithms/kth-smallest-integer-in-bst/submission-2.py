# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Recursive
        # count = 0
        # result = None
        # def recurse(node: TreeNode):
        #     nonlocal count, result
        #     if not node:
        #         return
        #     recurse(node.left)
        #     count += 1
        #     if count == k:
        #         result = node.val
        #         return
        #     recurse(node.right)
        
        # recurse(root)
        # return result

        # iterative
        stack = []
        cur = root
        n = 0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            result = stack.pop()
            n += 1
            if n == k:
                return result.val
            cur = result.right
        return 0