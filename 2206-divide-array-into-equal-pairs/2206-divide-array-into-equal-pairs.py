class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d.values():
            if i%2==1:
                return False
        return True