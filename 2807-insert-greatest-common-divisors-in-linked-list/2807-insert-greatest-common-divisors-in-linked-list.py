# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp,flag=head,0
        while(temp.next):
            x=temp.next
            temp.next=ListNode(math.gcd(temp.val,x.val))
            temp.next.next=x
            temp=temp.next.next
        return head