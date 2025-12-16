class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while(len(s)>2):
            st=""
            for i in range(len(s)-1):
                x=(int(s[i])+int(s[i+1]))%10
                st+=str(x)
            s=st
            print(s)
        if s[0]==s[1]:
            return True
        return False