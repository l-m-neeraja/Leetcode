class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mini=10**6
        for i in range(len(nums)-k+1):
            lst=[]
            for j in range(i,i+k):
                lst.append(nums[j])
            mini=min(mini,max(lst)-min(lst))
        return mini