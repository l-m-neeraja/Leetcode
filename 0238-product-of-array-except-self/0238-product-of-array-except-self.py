class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l,r=[1],[1]
        for i in range(len(nums)-1):
            r.append(r[-1]*nums[i])
        for i in range(len(nums)-1,0,-1):
            l.append(l[-1]*nums[i])
        ans=[]
        for i in range(len(nums)):
            ans.append(l[len(nums)-i-1]*r[i])
        return ans
        