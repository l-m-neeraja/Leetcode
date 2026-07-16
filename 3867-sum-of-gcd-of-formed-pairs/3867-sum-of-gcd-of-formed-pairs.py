class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        pf=[]
        maxi=-1
        for i in range(len(nums)):
            maxi=max(maxi,nums[i])
            pf.append(gcd(nums[i],maxi))
        pf.sort(reverse=True)
        res=0
        for i in range(len(pf)//2):
            res+=gcd(pf[i],pf[len(pf)-i-1])
        return res