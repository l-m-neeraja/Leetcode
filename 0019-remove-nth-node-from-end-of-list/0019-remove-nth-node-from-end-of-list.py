# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head==None or head.next==None:
            return None
        l=0
        temp=head
        while(temp):
            l+=1
            temp=temp.next
        t,x=l-n,0
        if t==x:
            return head.next
        temp=head
        while(temp):
            if x==t-1:
                if temp.next:
                    temp.next=temp.next.next
                break
            x+=1
            temp=temp.next
        
        return head