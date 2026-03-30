# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find the split of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # creating new list for second part
        # unlinking the mid.next from first part
        second = slow.next
        prev = slow.next = None

        # reversing the second list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # take both first and second list and remap the next
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2






        