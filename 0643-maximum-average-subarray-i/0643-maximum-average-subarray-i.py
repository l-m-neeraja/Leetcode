class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi,s,j=-10**5,0,k
        for i in range(k):
            s+=nums[i]
        maxi=max(maxi,s/k)
        i=0
        while j<len(nums):
            s-=nums[i]
            s+=nums[j]
            maxi=max(maxi,s/k)
            i,j=i+1,j+1
        return maxi
