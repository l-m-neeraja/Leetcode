class Solution:
    def maximumHappinessSum(self, arr: List[int], k: int) -> int:
        arr.sort()
        res=0
        for i in range(k):
            if arr[-1]-i<=0:
                res+=0
            else:
                res+=arr[-1]-i
            arr.pop()
        return res