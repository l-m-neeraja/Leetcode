class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        d={}
        for i in nums1:
            d[i]=1
        for i in nums2:
            if i in d:
                d[i]+=1
        mini=float('inf')
        for i in d.keys():
            if d[i]>=2:
                mini=min(mini,i)
        return mini if mini<=10**9 else -1
