class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while(n>=4):
            a=n%4
            if a!=0:
                break
            n=n//4
        if n==1:
            return True
        return False