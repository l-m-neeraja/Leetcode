class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        rmax = [0]*len(height)
        rmax[len(height)-1]=height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            rmax[i]=max(rmax[i+1],height[i])
        lmax = height[0]
        for i in range(1,len(height)-1):
            lmax=max(lmax,height[i])
            res+=min(lmax,rmax[i])-height[i]
        return res