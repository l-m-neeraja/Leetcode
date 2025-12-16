# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        lst=[]
        temp=head
        while(temp):
            lst.append(temp.val)
            temp=temp.next
        head = ListNode(lst[-1])
        temp=head
        for i in lst[len(lst)-2::-1]:
            temp.next=ListNode(i)
            temp=temp.next
        return head
