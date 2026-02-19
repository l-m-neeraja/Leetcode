class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        z,o=0,0
        res=0
        for i in range(len(s)-1):
            if s[i]=='1' and s[i+1]=='0':
                o+=1
                res+=min(z,o)
                z=0
            elif s[i]=='0' and s[i+1]=='1':
                z+=1
                res+=min(z,o)
                o=0
            else:
                if s[i]=='1':
                    o+=1
                else:
                    z+=1
        if s[-1]=='1':
            o+=1
        else:
            z+=1
        return res+min(z,o)