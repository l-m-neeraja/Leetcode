class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp=[]
        for i in range(len(grid)):
            dp.append([0]*len(grid[0]))
        dp[0][0]=grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j>0:
                    dp[i][j]=grid[i][j]+dp[i][j-1]
                elif i==0 and j==0:
                    continue
                elif j==0 and i>0:
                    dp[i][j]=grid[i][j]+dp[i-1][j]
                else:
                    dp[i][j]=grid[i][j]+min(dp[i][j-1],dp[i-1][j])
        return dp[len(grid)-1][len(grid[0])-1]