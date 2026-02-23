# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        lst=[]
        temp=head
        while temp!=None:
            lst.append(temp.val)
            temp=temp.next
        lst=lst[::-1]
        res=[lst[0]]
        for i in range(1,len(lst)):
            if lst[i]>=res[0]:
                res.insert(0,lst[i])
        head=ListNode(res[0],None)
        temp=head
        for i in range(1,len(res)):
            head.next=ListNode(res[i],None)
            head=head.next
        return temp