# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or not k:
            return head
        current=head
        length=1
        while current.next:
            current=current.next
            length+=1
        k=k%length
        if k==0:
            return head
        current1=head
        for i in range(length-k-1):
            current1=current1.next
        temp=current1.next
        current1.next=None
        current.next=head
        return temp
            
            

        
        