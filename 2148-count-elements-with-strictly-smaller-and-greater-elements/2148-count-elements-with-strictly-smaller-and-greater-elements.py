class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res=0
        for i in range(len(nums)):
            if nums[i]==nums[0] or nums[i]==nums[-1]:
                continue
            else:
                res+=1
        return res