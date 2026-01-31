class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.lstrip()
        s=s.rstrip()
        res=""
        temp=""
        for i in range(len(s)-1,-1,-1):
            if s[i]==" " and temp and temp[-1]!=" ":
                res+=temp[::-1]+" "
                temp=""
            elif s[i]!=" ":
                temp+=s[i]
        return res+temp[::-1]