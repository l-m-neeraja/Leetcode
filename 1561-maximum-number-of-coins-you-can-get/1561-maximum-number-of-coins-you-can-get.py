class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        x=len(piles)//3
        piles.sort()
        res=0
        for i in range(len(piles)-2,-1,-2):
            if x==0:
                break
            res+=piles[i]
            x-=1
        return res