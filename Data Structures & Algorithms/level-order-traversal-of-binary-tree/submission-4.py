# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        count = 1
        res = defaultdict(list)
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if node:
                    res[count].append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            count += 1
        return list(res.values())
            