# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # first create a function that would merge 2 ll
        # iterate through the lists but 2 items at a time, 
        # merge 2 ll and add it to res

        while len(lists) > 1:
            res = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                res.append(self.mergeLL(list1,list2))
            lists = res
        return lists[0] if len(lists) != 0 else None
    
    def mergeLL(self, list1, list2):
        head = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        
        if list1:
            dummy.next = list1
            dummy = dummy.next
        if list2:
            dummy.next = list2
            dummy = dummy.next
        return head.next




             

        