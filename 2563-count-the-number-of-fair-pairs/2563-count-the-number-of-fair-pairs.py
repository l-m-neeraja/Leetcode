class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        u,o=0,0
        l,h=0,len(nums)-1
        while(l<=h):
            if nums[l]+nums[h]<=upper:
                o+=h-l
                l+=1
            else:
                h-=1
        l,h=0,len(nums)-1
        while(l<=h):
            if nums[l]+nums[h]<lower:
                u+=h-l
                l+=1
            else:
                h-=1
        return o-u       