class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        s = str(bin(start)).replace("0b","")
        g = str(bin(goal)).replace("0b","")
        d = max(len(s),len(g)) - min(len(s),len(g))
        for i in range(d):
            if(min(len(s),len(g))==len(g)):
                g="0"+g
            else:
                s="0"+s
        x=0
        for i in range(len(g)):
            if s[i] != g[i]:
                x+=1
        return x