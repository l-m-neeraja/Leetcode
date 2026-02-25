# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next==None:
            return
        cnt=0
        temp=head
        while temp!=None:
            cnt+=1
            temp=temp.next
        temp=head
        x=0
        while x<cnt//2 -1:
            x+=1
            temp=temp.next
        temp.next=temp.next.next
        return head