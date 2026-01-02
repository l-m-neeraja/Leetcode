class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        x=len(nums)//2
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            if d[i]==x:
                return i