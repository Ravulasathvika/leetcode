/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        if(head==null)
        {
            return head;
        }
        ListNode p=null;
        ListNode q=null;
        ListNode r=head;
        for(int i=1;i<k;i++)
        {
            r=r.next;
            
        }
        p=r;
        q=head;
        while(r.next!=null)
        {
            q=q.next;
            r=r.next;
        }
        int temp=p.val;
        p.val=q.val;
        q.val=temp;
        return head;
        
        
    }
}