class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        for i in s:
            if i not in d:
                d[i]=1
        return len(d.keys())