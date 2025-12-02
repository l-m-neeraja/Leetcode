class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        n=len(moves)
        a=[0,0]
        for i in range(n):
            if moves[i]=='U':
                a[1]+=1
            elif moves[i]=='D':
                a[1]-=1
            elif moves[i]=='R':
                a[0]+=1
            else:
                a[0]-=1
        if a[0]==a[1]==0:
            return True
        return False