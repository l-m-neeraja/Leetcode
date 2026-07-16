class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lst=[]
        for i in range(1,max(arr)):
            lst.append(i)
        res=[]
        for i in lst:
            if i not in arr:
                res.append(i)
        i=max(arr)+1
        while len(res)<k:
            res.append(i)
            i+=1
        return res[k-1]