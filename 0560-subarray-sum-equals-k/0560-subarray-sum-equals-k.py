class Solution(object):
    def subarraySum(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(1,len(arr)):
            arr[i] += arr[i-1]
        count = 0
        d = {0:1}
        for i in range(len(arr)):
            x = arr[i]
            y = arr[i] - k
            if y in d:
                count += d[y]  
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        return count