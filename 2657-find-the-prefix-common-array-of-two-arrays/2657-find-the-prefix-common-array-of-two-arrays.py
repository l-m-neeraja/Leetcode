class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        i=0
        d={}
        d2={}
        res=[0]
        while i<len(A):
            x=0
            if A[i]==B[i]:
                x+=1
            else:
                if A[i] in d2:
                    x+=1
                if B[i] in d:
                    x+=1
            d[A[i]]=1
            d2[B[i]]=1
            res.append(res[-1]+x)
            i+=1
        return res[1:]