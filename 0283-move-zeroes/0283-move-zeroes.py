class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cnt=0
        lst=[]
        for i in nums:
            if i==0:
                cnt+=1
            else:
                lst.append(i)
        for i in range(cnt):
            lst.append(0)
        nums[:]=lst
        