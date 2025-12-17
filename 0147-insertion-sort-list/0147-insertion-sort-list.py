# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head==None:
            return None
        lst=[]
        temp=head
        while(temp):
            lst.append(temp.val)
            temp=temp.next
        lst.sort()
        head=ListNode(lst[0])
        temp=head
        for i in range(1,len(lst)):
            temp.next=ListNode(lst[i])
            temp=temp.next
        return head