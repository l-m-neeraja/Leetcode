class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j=0,len(nums)-1
        while i<j:
            x=nums[i]+nums[j]
            if x==target:
                return [i+1,j+1]
            elif x>target:
                j-=1
            else:
                i+=1