class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=[nums[0]]
        for i in range(1,len(nums)):
            p.append(p[i-1]+nums[i])
        if p[-1]-p[0]==0:
            return 0
        print(p)
        for i in range(1,len(nums)):
            if i==len(nums)-1:
                if p[-2]==0:
                    return i
            elif p[i-1]==p[-1]-p[i]:
                return i
        return -1