class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res=0
        x^=y
        for i in range(32):
            if x>(x^1):
                res+=1
            x>>=1
        return res