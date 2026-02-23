class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.lstrip()
        if len(s)==0:
            return 0
        if s[0]=='-':
            a=-1
        else:
            a=1
        if s[0]=='-' or s[0]=='+':
            if len(s)==1:
                return 0
            s=s[1:]
        b=""
        if ord(s[0])>=48 and ord(s[0])<=57:
            b+=s[0]
            for i in range(1,len(s)):
                if ord(s[i])>=48 and ord(s[i])<=57:
                    b+=s[i]
                else:
                    break
        else:
            return 0
        if a*int(b)< -2**31:
            return -2**31
        if a*int(b)>(2**31)-1:
            return (2**31)-1
        return a*int(b)