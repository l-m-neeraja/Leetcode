class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        x=n
        for i in range(32):
            if x&1==1:
                k=i
            x>>=1
        alt=1
        for _ in range(k):
            alt|=1
            alt<<=1
        alt|=1
        return n^alt