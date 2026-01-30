# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        res,k=0,0
        i=0
        while head!=None:
            res+=(2**(29-i))*head.val
            k+=1
            head=head.next
            i+=1
        return res>>(30-k)
        