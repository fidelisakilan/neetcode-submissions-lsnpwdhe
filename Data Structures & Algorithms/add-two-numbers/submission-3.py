# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0, None)
        node = dummy
        while l1 or l2:
            a = 0
            b = 0
            if l1 is not None:
                a = l1.val
                l1 = l1.next
            if l2 is not None:
                b = l2.val
                l2 = l2.next
            total = a + b + carry
            dig = total % 10
            node.next = ListNode(dig, None)
            carry = int((total - dig) / 10)
            print(total, dig, carry)
            node = node.next
        if carry:
            node.next = ListNode(carry, None)
        return dummy.next
