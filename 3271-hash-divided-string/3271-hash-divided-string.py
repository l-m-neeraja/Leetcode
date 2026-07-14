class Solution:
    def stringHash(self, s: str, k: int) -> str:
        d={}
        for i in range(26):
            d[chr(97+i)]=i
        res=""
        for i in range(0,len(s)-k+1,k):
            t=0
            for j in range(k):
                t+=d[s[i+j]]
            t=t%26
            res+=chr(97+t)
        return res