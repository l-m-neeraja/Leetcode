class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=int(s,2)
        cnt=0
        while n>1:
            cnt+=1
            if n%2==1:
                n+=1
            else:
                n>>=1
        return cnt