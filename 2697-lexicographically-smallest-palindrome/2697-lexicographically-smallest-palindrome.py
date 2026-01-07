class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        i,j=0,len(s)-1
        while i<j:
            if s[i]!=s[j]:
                if s[i]>s[j]:
                    st=s[:i]+s[j]+s[i+1:]
                    s=st
                else:
                    st=s[:j]+s[i]+s[j+1:]
                    s=st
            i+=1
            j-=1
        return s