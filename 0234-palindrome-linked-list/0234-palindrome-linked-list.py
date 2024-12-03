# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        current=head
        sum1=[]
        while current:
            sum1.append(current.val)
            current=current.next
        
        return sum1==sum1[::-1]
            