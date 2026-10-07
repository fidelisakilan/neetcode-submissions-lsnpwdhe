"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        adjlist = {}

        def dfs(node):
            if not node:
                return None
            if node in oldToNew:
                return oldToNew[node]
            new_node = Node(node.val)
            res = []
            oldToNew[node] = new_node
            for nei in node.neighbors:
                child = dfs(nei)
                if child:
                    res.append(child)
            new_node.neighbors = res
            return new_node

        return dfs(node)