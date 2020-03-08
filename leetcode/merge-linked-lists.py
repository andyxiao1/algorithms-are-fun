# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # splice into l1
        
        if not l1:
            return l2
        elif not l2:
            return l1
        
        p1 = l1
        first = l1
        
        if l2.val < l1.val:
            first = l2
            l1, l2 = l2, l1
        
        while l1 and l2:
            if l2.val >= l1.val:
                p1 = l1
                l1 = l1.next
            else:
                tmp = l2.next
                p1.next = l2
                l2.next = l1
                p1 = l2
                l2 = tmp
        
        if l2:
            p1.next = l2
        return first