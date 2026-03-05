class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        while(n):
            if n%3!=0:
                break
            n//=3
        return n==1