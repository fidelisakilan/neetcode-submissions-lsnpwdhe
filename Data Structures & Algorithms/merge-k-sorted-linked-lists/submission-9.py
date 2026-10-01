# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        res1 = []
        counter = 0
        for l in lists:
            if l is not None:
                heapq.heappush(res1, (l.val,counter, l))
                counter += 1
        
        if len(res1) == 0:
            return None
        
        while res1:
            v, _, node = heapq.heappop(res1)
            curr.next = node
            curr = curr.next
            if node.next != None:
                heapq.heappush(res1, (node.next.val, counter, node.next))
                counter += 1
        
        return dummy.next
        