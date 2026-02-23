class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        l=set()
        for i in range(len(s)-k+1):
            l.add(s[i:i+k])
        return len(l)==2**k