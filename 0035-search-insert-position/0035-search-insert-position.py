class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0]==target or nums[0]>target:
            return 0
        if len(nums)>=2:
            if nums[0]<target and nums[1]>target:
                return 1
        for i in range(1,len(nums)):
            if nums[i-1]<target and nums[i]>=target:
                return i
        if nums[len(nums)-1]==target:
            return len(nums)-1
        if nums[len(nums)-1]<target:
            return len(nums)