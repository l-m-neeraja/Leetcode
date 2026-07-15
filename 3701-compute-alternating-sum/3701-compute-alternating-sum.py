class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f=-1
        res=nums[0]
        for i in range(1,len(nums)):
            res+=f*nums[i]
            f*=-1
        return res