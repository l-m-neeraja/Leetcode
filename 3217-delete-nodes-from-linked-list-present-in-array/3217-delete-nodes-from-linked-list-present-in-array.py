# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums=set(nums)
        temp=head
        x=ListNode(0,None)
        temp2=x
        while temp!=None:
            if temp.val not in nums:
                temp2.next=ListNode(temp.val,None)
                temp2=temp2.next
            temp=temp.next
        return x.next