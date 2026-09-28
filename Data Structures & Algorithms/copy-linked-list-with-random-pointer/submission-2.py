"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapper = {}
        visited = {}
        def recurse(node):
            if not node:
                return None
            if node not in mapper:
                mapper[node] = Node(node.val)
            else:
                return mapper[node]
            copy = mapper[node]
            if node.next:
                copy.next = recurse(node.next)
            if node.random:
                copy.random = recurse(node.random)
            
            return copy
        return recurse(head)

        