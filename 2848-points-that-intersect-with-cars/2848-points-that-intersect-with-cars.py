class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        nums.sort(key=lambda x: x[1])
        lst=[0]*(nums[-1][1]+1)
        for i in nums:
            lst[i[0]-1]+=1
            lst[i[1]]-=1
        cnt=0 if lst[0]==0 else 1
        for i in range(1,len(lst)-1):
            lst[i]+=lst[i-1]
            if lst[i]>0:
                cnt+=1
        return cnt