class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lst=[]
        for i in range(len(s)):
            lst.append(s[i]+t[i])
        mini=min(len(set(s)),len(set(t)))
        return len(set(lst))==mini
