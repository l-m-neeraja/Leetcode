class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        if n<4:
            return False
        flag=1
        x=False
        for i in range(n-1):
            if flag==1:
                if nums[i]<nums[i+1]:
                    x=True
                elif nums[i]>nums[i+1]:
                    if not x:
                        return False
                    flag=2
                else:
                    return False
            elif flag==2:
                if nums[i]>nums[i+1]:
                    continue
                elif nums[i]<nums[i+1]:
                    flag=3
                else:
                    return False
            else:
                if nums[i]< nums[i+1]:
                    continue
                else:
                    return False
        return flag==3