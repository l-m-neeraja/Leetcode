class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        res="1"
        for i in range(2,n+1):
            res+=bin(i)[2:]
        return int(res,2)%((10**9)+7)