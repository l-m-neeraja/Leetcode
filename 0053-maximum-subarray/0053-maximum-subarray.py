class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr,res=nums[0],nums[0]
        for i in range(1,len(nums)):
            curr = max(curr+nums[i],nums[i])
            res=max(res,curr)
        return res