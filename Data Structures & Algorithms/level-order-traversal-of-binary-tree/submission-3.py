# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [(root, 0)]
        res = []

        while stack:
            for i in range(len(stack)):
                node, index = stack.pop()
                if not node:
                    continue
                if node.right:
                    stack.append((node.right, index+1))
                if node.left:
                    stack.append((node.left, index+1))
                if len(res) <= index:
                    res.append([])
                res[index].append(node.val)
        return res




        