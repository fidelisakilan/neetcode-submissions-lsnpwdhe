# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        result = []
        while q:
            l = len(q)
            last_val = None
            for i in range(l):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    last_val = node.val
            if last_val:
                result.append(last_val)
        return result

