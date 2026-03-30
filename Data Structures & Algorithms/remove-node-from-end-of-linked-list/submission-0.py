# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        print(count, n, count - n)

        if count == n:
            return head.next

        prev, curr = head, head
        steps = count - n - 1
        while steps:
            prev = curr
            curr = curr.next
            steps -= 1
        curr.next = curr.next.next
        return head