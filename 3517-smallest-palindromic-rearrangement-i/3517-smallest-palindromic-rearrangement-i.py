class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        res=''
        lst=d.keys()
        lst.sort()
        x=''
        for i in lst:
            if d[i]%2==1:
                x+=i
            res+=i*(d[i]//2)
        return res+x+res[::-1]