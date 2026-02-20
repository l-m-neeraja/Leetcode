class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(1,len(nums)+1):
            if i<len(nums):
                if i<=nums[-i] and i>nums[-i-1]:
                    return i
            else:
                if i<=nums[-i]:
                    return i
        return -1