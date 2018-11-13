# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a=headA
        b=headB
        la=lb=0
        while (a):
            la+=1
            a=a.next
        while(b):
            lb+=1
            b=b.next
            
        a = headA
        b = headB
        if la>lb:
            c=la-lb
            while c>0:
                a=a.next
                c-=1
        else:
            c=lb-la
            while c>0:
                b=b.next
                c-=1
        
        while a!=b:
            a=a.next
            b=b.next
            
        return a
        
            
            
        
            
                
        