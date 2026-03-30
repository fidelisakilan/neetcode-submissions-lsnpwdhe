# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # # BFS
        # q = collections.deque()
        # q.append(root)
        # result = []
        # while q:
        #     qLen = len(q)
        #     level = []
        #     for i in range(qLen):
        #         node = q.popleft()
        #         if node:
        #             level.append(node.val)
        #             q.append(node.left)
        #             q.append(node.right)
        #     if level:
        #         result.append(level)
        # return result
        result = []
        def dfs(node: Optional[TreeNode], level: int):
            if not node:
                return None
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return result
                    
                


        