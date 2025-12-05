class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        for i in range(len(nums)):
            d[i+1]=0
        for i in nums:
            d[i]+=1
        res=[0,0]
        for i in d.keys():
            if d[i]==2:
                res[0]=i
            elif d[i]==0:
                res[1]=i
        return res