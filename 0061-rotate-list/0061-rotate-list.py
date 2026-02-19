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
        if not head: 
            return None
        cnt=0
        temp=head
        while temp!=None:
            cnt+=1
            temp=temp.next
        if k==0 or k%cnt==0:
            return head
        x=k%cnt
        temp=head
        for _ in range(cnt-x-1):
            temp=temp.next
        tempnxt=temp.next
        temp.next=None
        temp=tempnxt
        while temp!=None and temp.next!=None:
            temp=temp.next
        if temp:
            temp.next=head
        return tempnxt