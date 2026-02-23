# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head==None:
            return None
        a=head.val
        temp=head.next
        lst=[a]
        k=1
        while(temp!=None):
            if lst:
                if lst[-1]!=temp.val:
                    if k>1:
                        for i in range(k):
                            x=lst.pop()

                        k=1
                    lst.append(temp.val)
                else:
                    k+=1
                    lst.append(temp.val)
            else:
                lst.append(temp.val)
                k=1
            temp=temp.next
        if k>1:
            for i in range(k):
                x=lst.pop()
        if (len(lst)>1 and len(set(lst))==1) or not lst:
            return None
        temp=ListNode(lst[0],None)
        ex=temp
        for i in range(1,len(lst)):
            temp.next=ListNode(lst[i],None)
            temp=temp.next
        return ex