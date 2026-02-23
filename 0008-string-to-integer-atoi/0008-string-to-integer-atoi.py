class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        s=s.lstrip()
        if len(s)==0:
            return 0
          
        if s[0]=='-':
            a=-1
        else:
            a=1
        if s[0]=='-' or s[0]=='+':
            s=s[1:]
        if len(s)==0:
            return 0
        b=""
        if ord(s[0])>=48 and ord(s[0])<=57:
            for i in s:
                if ord(i)>=48 and ord(i)<=57:
                    b+=i
                else:
                    break
        else:
            return 0
        if a*int(b)< -2**31:
            return -2**31
        if a*int(b)>(2**31)-1:
            return (2**31)-1
        return a*int(b)