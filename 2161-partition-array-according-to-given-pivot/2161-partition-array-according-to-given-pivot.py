class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        lst=[]
        lst2=[]
        lst3=[]
        for i in nums:
            if i < pivot:
                lst.append(i)
        for i in nums:
            if i == pivot:
                lst2.append(i)
        for i in nums:
            if i > pivot:
                lst3.append(i)
        return lst+lst2+lst3
