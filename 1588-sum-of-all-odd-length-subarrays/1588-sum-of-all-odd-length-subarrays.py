class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res=0
        for i in range(len(arr)):
            s,e = i+1,len(arr)-i
            a=(s*e+1)//2
            res+=a*arr[i]
        return res