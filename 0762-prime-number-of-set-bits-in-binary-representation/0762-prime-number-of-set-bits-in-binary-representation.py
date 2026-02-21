class Solution(object):
    def noBits(self,x):
        res=0
        while x:
            res+=x&1
            x=x>>1
        return res
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        res=0
        for i in range(left,right+1):
            if self.noBits(i) in [2, 3, 5, 7, 11, 13, 17,19]:
                res+=1
        return res