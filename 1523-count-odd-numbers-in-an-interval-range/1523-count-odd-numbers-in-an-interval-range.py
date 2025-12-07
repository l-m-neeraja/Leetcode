class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        cnt=0
        if low % 2 == 1 or high % 2 == 1:
            cnt = (high - low) // 2 + 1  
        else:
            cnt=(high - low) // 2
        return cnt