# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        temp=dummy
        current=head
        current=current.next
        s=0
        while current:
            if current.val==0:
                temp.next=ListNode(s)
                temp=temp.next
                s=0
            s+=current.val
            current=current.next
        return dummy.next
                
        