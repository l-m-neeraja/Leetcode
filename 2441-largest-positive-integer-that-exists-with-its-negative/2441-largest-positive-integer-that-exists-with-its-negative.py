class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst=[]
        for i in nums:
            if i>0 and -i in nums:
                lst.append(i)
        return max(lst) if lst else -1