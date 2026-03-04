class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]]=[i]
        print(d)
        for i in d.values():
            for j in range(len(i)-1):
                if i[j+1]-i[j]<=k:
                    return True
        return False