class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        flag,flag2=0,0
        while i<=j:
            if s[i]!=s[j]:
                flag+=1
                i-=1
            i+=1
            j-=1
        i,j=0,len(s)-1
        while i<=j:
            if s[i]!=s[j]:
                flag2+=1
                j+=1
            i+=1
            j-=1
        return min(flag,flag2)<2