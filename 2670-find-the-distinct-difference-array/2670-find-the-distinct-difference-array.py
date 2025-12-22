class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[0]*len(nums)
        for i in range(len(nums)):
            p,s=set(nums[:i+1]),set(nums[i+1:len(nums)])
            res[i]=len(p)-len(s)
        return res