# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp=node
        while temp.next!= None:
            temp.val=temp.next.val
            temp=temp.next
        temp=node
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None