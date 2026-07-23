class Solution(object):
    def longestCommonPrefix(self, lst):
        """
        :type strs: List[str]
        :rtype: str
        """
        m=250
        for i in lst:
            m=min(m,len(i))
        a=0
        s=""
        for i in range(m):
            for j in lst:
                if j[i]==lst[0][i]:
                    a=1
                else:
                    a=0
                    break
            if a==1:
                s+=lst[0][i]
            else:
                break
        return s
            
