# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        lst=[]
        temp=head
        while temp:
            lst.append(temp.val)
            temp=temp.next
        i,j=0,len(lst)-1
        temp=head
        for k in range(len(lst)):
            if k%2==0:
                temp.val=lst[i]
                i+=1
            else:
                temp.val=lst[j]
                j-=1
            temp=temp.next