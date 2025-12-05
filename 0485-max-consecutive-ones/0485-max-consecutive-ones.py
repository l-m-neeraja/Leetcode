class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        maxi=0
        for i in nums:
            if i==0:
                res=0
            else:
                res+=1
                maxi=max(maxi,res)
        return maxi