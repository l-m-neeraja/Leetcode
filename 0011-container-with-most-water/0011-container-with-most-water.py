class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r = 0,len(height)-1
        maxi=0
        while l<r:
            a = r-l
            h = min(height[l],height[r])
            maxi= max(maxi,h*a)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maxi