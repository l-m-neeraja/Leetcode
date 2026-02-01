class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=sorted(nums[1::])
        return nums[0]+x[0]+x[1]