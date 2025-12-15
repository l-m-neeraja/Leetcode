# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l=0
        temp=head
        while(temp):
            l+=1
            temp=temp.next
        n=l//2 + 1
        x,temp=0,head
        while(temp):
            if x==n-1:
               return temp
            x+=1
            temp=temp.next
        