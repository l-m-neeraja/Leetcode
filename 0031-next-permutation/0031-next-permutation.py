class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                p=i
                break
        if p==-1:
            nums.sort()
        else:
            for i in range(len(nums)-1,-1,-1):
                if nums[p]<nums[i]:
                    nums[p],nums[i]=nums[i],nums[p]
                    break
            temp=nums[p+1:]
            temp.sort()
            nums[p+1:]=temp