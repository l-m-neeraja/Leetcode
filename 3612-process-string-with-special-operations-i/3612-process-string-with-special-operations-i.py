class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        for i in s:
            if i=='*':
                if res:
                    res=res[:-1]
            elif i=='#':
                res=res+res
            elif i=='%':
                res=res[::-1]
            else:
                res+=i
        return res