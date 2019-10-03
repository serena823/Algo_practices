# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1 
        if l1 is None and l2 is None:
            return None 
        
        dummy = ListNode(0)
        temp  = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2 
                l2 = l2.next
            temp = temp.next
        if l1 != None:
            temp.next = l1
        if l2 != None:
            temp.next = l2
        return dummy.next
        