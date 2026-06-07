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
        oldToNext = {None: None}

        curr = head
        while curr:
            node = Node(curr.val)
            oldToNext[curr] = node
            curr = curr.next
        
        curr = head
        while curr:
            node = oldToNext[curr]
            node.next = oldToNext[curr.next]
            node.random = oldToNext[curr.random]
            curr = curr.next
        
        return oldToNext[head]
