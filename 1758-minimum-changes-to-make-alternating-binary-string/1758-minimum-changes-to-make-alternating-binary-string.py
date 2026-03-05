class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1,s2="",""
        for i in range(len(s)):
            if i%2==0:
                s1+="1"
                s2+="0"
            else:
                s2+="1"
                s1+="0"
        c1,c2=0,0
        for i in range(len(s)):
            if s[i]!=s1[i]:
                c1+=1
            elif s[i]!=s2[i]:
                c2+=1
        return min(c1,c2)