class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for i in range(len(nums)-1):
            if (sum(nums[:i+1])+sum(nums[i+1:]) )%2==0:
                res+=1
        return res