class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp=[cost[0],cost[1]]
        for i in range(2,len(cost)):
            x=min(dp[i-1],dp[i-2])
            dp.append(x+cost[i])
        return min(dp[-1],dp[-2])