class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ld=head
        while ld:
            if ld.next and ld.next.val==ld.val:
                ld.next=ld.next.next
            else:
                ld=ld.next
        return head

