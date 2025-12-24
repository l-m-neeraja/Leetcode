class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        maxi,res=0,""
        for i in range(len(s)):
            for j in range(i,len(s)):
                st=s[i:j+1]
                n=len(set(st.lower()))
                if len(set(st))==2*n:
                    if len(st)>maxi:
                        res=st
                        maxi=len(st)
        return res