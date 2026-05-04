"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        oldToNew = {}

        def dfs(node):
            if node.val not in oldToNew:
                oldToNew[node.val] = Node(node.val,[])
            
            newNode = oldToNew[node.val]
            for child in node.neighbors:
                if child.val not in oldToNew:
                    dfs(child)
                newNode.neighbors.append(oldToNew[child.val])
            return newNode
        return dfs(node)
        