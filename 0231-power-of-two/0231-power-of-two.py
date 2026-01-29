class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1:
            return False
        res=0
        for i in range(32):
            res+=(n&1)
            n>>=1
        return res==1