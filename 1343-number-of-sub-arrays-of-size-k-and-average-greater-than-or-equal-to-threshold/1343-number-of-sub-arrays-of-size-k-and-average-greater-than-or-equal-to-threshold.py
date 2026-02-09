class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        cnt=0
        avg=0
        for i in range(k):
            avg+=arr[i]
        if avg>=threshold*k:
            cnt+=1
        for i in range(k,len(arr)):
            avg+=arr[i]-arr[i-k]
            if avg>=threshold*k:
                cnt+=1
        return cnt