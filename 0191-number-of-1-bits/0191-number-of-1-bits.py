class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        for i in range(32):
            c+=(n&1)
            n>>=1
        return c