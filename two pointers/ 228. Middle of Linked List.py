"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        # write your code here
        if head is None:
            return None
   
        slow = head
        fast = slow.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
            
            
###########################
# two pointers 
# fast and slow one
# fast move two steps while slow move one step
# fast get the end and slow is mid
#############################

            
        