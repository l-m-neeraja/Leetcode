class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        for i in range(len(s)-2):
            lst=[]
            for j in range(i,i+3):
                if s[j] in lst:
                    break
                else:
                    lst.append(s[j])
            if len(lst)==3:
                res+=1
        return res