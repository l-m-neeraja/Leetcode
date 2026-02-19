class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        x=""
        for i in s:
            if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):
                x+=i
        x=x[::-1]
        res=""
        j=0
        for i in s:
            if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):
                res+=x[j]
                j+=1
            else:
                res+=i
        return res